from hem_app.models import Dose, Category, RunParams, RunHistory, Chemical, Person
import pandas as pd
from datetime import datetime


def get_dose_qs(h):
	history = RunHistory.objects.get(pk=h)

	# first filter by age and gender from the form
	if history.gender == 'B':
		dose = Dose.objects.filter(person__age_years__gte=history.min_age, person__age_years__lte=history.max_age)
	else:
		dose = Dose.objects.filter(person__age_years__gte=history.min_age, person__age_years__lte=history.max_age,
								   person__gender=history.gender)

	dose = dose.values('runparams', 'chemical__cas', 'chemical__title', 'person_id', 'person__gender',
					   'person__age_years', 'day', 'dir_derm_exp', 'dir_derm_max', 'dir_derm_abs', 'dir_inhal_exp',
					   'dir_inhal_mass', 'dir_inhal_max', 'dir_inhal_abs', 'dir_ingest_exp', 'dir_ingest_abs',
					   'release', 'ind_derm_exp', 'ind_derm_max', 'ind_derm_abs', 'ind_inhal_exp', 'ind_inhal_max',
					   'ind_inhal_mass', 'ind_inhal_abs', 'ind_ingest_exp', 'ind_ingest_abs', 'out_sur', 'out_air',
					   'drain', 'waste')

	# Process dose for chemical
	if history.is_product == 0:
		# find the run params id for the category with all products
		rp = RunParams.objects.filter(category__category__runparams=None).first().id
		chem_id = Chemical.objects.get(pk=history.chemical_id)
		dose = dose.filter(chemical_id=chem_id, runparams_id=rp)
	else:
		rp = RunParams.objects.filter(product_id=history.product_id).first().id
		dose = dose.filter(runparams_id=rp)
	return dose


def get_population_qs(h):
	history = RunHistory.objects.get(pk=h)
	if history.gender == 'B':
		population = Person.objects.filter(age_years__gte=history.min_age,
										   age_years__lte=history.max_age).values('id', 'gender', 'race', 'ethnicity',
																				 'age_years', 'ages', 'genders',
																				 'baths', 'lot', 'dishwash', 'cwasher',
																				 'swim')
	else:
		population = Person.objects.filter(age_years__gte=history.min_age, age_years__lte=history.max_age,
										   gender=history.gender).values('id', 'gender', 'race', 'ethnicity',
																		 'age_years', 'ages', 'genders',  'baths',
																		 'lot', 'dishwash', 'cwasher', 'swim')

	print(population.count())
	return population


def get_chemical_data(chemical, run_history):
	# filter to get the people selected in form
	################################
	# TODO This block is taking way too long
	population = get_population_qs(run_history.id)
	population_ids = population.values('id')
	if run_history.is_product == 0:
		# only grab the dose for All products run params
		all_cat_id = int(Category.objects.filter(parent_id=None).first().id)
		run_params_id = int(RunParams.objects.filter(category_id=all_cat_id).first().id)

	else:
		# only grab the dose for the chemical
		run_params_id = int(RunParams.objects.filter(product_id=run_history.product_id).first().id)
	print('end runparams, start pop with dose :' + str(datetime.now()))

	# TODO First operand needs to be total people of age and gender of interest
	population_with_dose = population.filter(dose__runparams_id=run_params_id,
												 dose__chemical=chemical).distinct().count()
	print("population with dose = " + str(population_with_dose))
	print('end pop with dose, start null pop :' + str(datetime.now()))

	# TODO First operand needs to be total people of age and gender of interest
	population_null = population.count() - population_with_dose
	print("population null = " + str(population_null))
	print('end null pop, start dose :' + str(datetime.now()))
	dose = Dose.objects.filter(person_id__in=population_ids)
	print('end dose, start more dose :' + str(datetime.now()))
	dose = dose.filter(chemical_id=chemical,
					   runparams_id=run_params_id).values('id', 'day', 'dir_derm_abs', 'dir_ingest_abs',
														  'dir_inhal_abs', 'ind_derm_abs', 'ind_inhal_abs',
														  'ind_ingest_abs')
	print('end more dose, start data :' + str(datetime.now()))
	data = pd.DataFrame(list(dose))
	print('end data :' + str(datetime.now()))
	# This block is taking way to long
	############################

	# Magic from Katherine Phillips
	# data = data[['id','day','dir_derm_abs','dir_ingest_abs','dir_inhal_abs','ind_derm_abs','ind_inhal_abs','ind_ingest_abs']].copy()
	# the year in the model is only 364 days. WTF? This is how science works.
	n_days = 364
	# get the next person id available to the dataframe
	person_next_id = Person.objects.all().order_by("-id")[0].id + 1
	n_people = person_next_id
	data_null = pd.DataFrame({'id': pd.np.repeat(pd.np.arange(0, population_null) + n_people, n_days),
							  "day": pd.np.tile(pd.np.arange(1, n_days + 1), population_null),
							  "dir_derm_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "dir_ingest_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "dir_inhal_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "ind_derm_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "ind_inhal_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "ind_ingest_abs": pd.np.zeros(shape=(population_null * n_days))})
	data_null = data_null[['id', 'day', 'dir_derm_abs', 'dir_ingest_abs', 'dir_inhal_abs', 'ind_derm_abs',
						   'ind_inhal_abs', 'ind_ingest_abs']].copy()
	# Combine data and data_null into one DataFrame
	data = pd.concat([data, data_null])
	data['day_sys_dose'] = data.dir_derm_abs + data.dir_ingest_abs + data.dir_inhal_abs + data.ind_derm_abs + \
						   data.ind_inhal_abs + data.ind_ingest_abs
	ann_sys_dose = data.groupby(['id']).day_sys_dose.mean().reset_index()
	weights = pd.np.ones_like(ann_sys_dose.day_sys_dose.tolist()) / len(ann_sys_dose.day_sys_dose.tolist())
	hist, bin_edges = pd.np.histogram(ann_sys_dose.day_sys_dose, weights=weights * 100, bins=50)
	bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.
	cum_dist = pd.np.cumsum(hist)

	json_data = {'dose': []}

	for i in range(0, len(cum_dist)):
		json_data['dose'].append([cum_dist[i], bin_centers[i]])

	return json_data


