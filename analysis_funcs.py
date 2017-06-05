from hem_app.models import Dose, Category, RunParams, LifeCycleImpact, RunHistory, Chemical, Person
import pandas as pd


def get_person_nulls(run_history):
	'''
	Given a run history return total_people, total_nulls, total_dosed
	Args:
		run_history = the run history from the form

	Returns:
		total {people, nulls,
	'''



def get_lcia_qs(h):
	history = RunHistory.objects.get(pk=h)
	# find the run params id for the category in runhistory
	rp = RunParams.objects.filter(category=history.categories).first()
	# all rows in lifecycle that have the run params id
	lcia = LifeCycleImpact.objects.filter(runparams_id=rp.id).values('chemical__cas', 'chemical__title', 'runparams_id',
																	 'mass_frac_chem_puc', 'mass_puc_use_adult',
																	 'pif_derm_adult', 'pif_inhal_adult',
																	 'pif_inhal_adult', 'mass_puc_use_child',
																	 'pif_derm_child', 'pif_inhal_child',
																	 'pif_ingest_child', 'chem_mass',
																	 'mass_tot_air', 'mass_tot_water',
																	 'mass_tot_land', 'product__category__title',
																	 'product__title')

	return lcia


def get_dose_qs(h):
	history = RunHistory.objects.get(pk=h)
	# first filter by age and gender from the form
	if history.gender == 'B':
		dose = Dose.objects.filter(person__age_years__gte=history.min_age, person__age_years__lte=history.max_age)
	else:
		dose = Dose.objects.filter(person__age_years__gte=history.min_age, person__age_years__lte=history.max_age,
								   person__gender=history.gender)

	# Process dose for chemical
	if history.products == 0:
		chem_id = Chemical.objects.get(pk=history.chemical_id)
		dose = dose.filter(chemical_id=chem_id)
	# TODO process dose for product
	else:
		dose = dose

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
	return population


def get_chemical_data(chemical):

	#TODO Apply form variables
	#TODO Count People - This might go in the view prior to entry here

	# only grab the dose for All products run params
	all_cat_id = int(Category.objects.filter(parent_id=None).first().id)
	run_params_id = int(RunParams.objects.filter(category_id=all_cat_id).first().id)

	dose = Dose.objects.filter(chemical_id=chemical, runparams_id=run_params_id).values('id', 'day', 'dir_derm_abs',
																						'dir_ingest_abs',
																						'dir_inhal_abs')

	data = pd.DataFrame(list(dose))

	population_null = 8000

	# Magic from Katherine Phillips
	data = data[['id', 'day', 'dir_derm_abs', 'dir_ingest_abs', 'dir_inhal_abs']].copy()


	n_days = 364
	#TODO this next line should be the next id available to the dataframe
	n_people = 109999999
	data_null = pd.DataFrame({'id': pd.np.repeat(pd.np.arange(0, population_null) + n_people, n_days),
							  "day": pd.np.tile(pd.np.arange(1, n_days + 1), population_null),
							  "dir_derm_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "dir_ingest_abs": pd.np.zeros(shape=(population_null * n_days)),
							  "dir_inhal_abs": pd.np.zeros(shape=(population_null * n_days))})
	data_null = data_null[['id', 'day', 'dir_derm_abs', 'dir_ingest_abs', 'dir_inhal_abs']].copy()

	## Combine data and data_null into one DataFrame
	data = pd.concat([data, data_null])
	data['day_sys_dose'] = data.dir_derm_abs + data.dir_ingest_abs + data.dir_inhal_abs

	ann_sys_dose = data.groupby(['id']).day_sys_dose.mean().reset_index()
	weights = pd.np.ones_like(ann_sys_dose.day_sys_dose.tolist()) / len(ann_sys_dose.day_sys_dose.tolist())
	hist, bin_edges = pd.np.histogram(ann_sys_dose.day_sys_dose, weights=weights * 100, bins=20)
	bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.
	cum_dist = pd.np.cumsum(hist)


	json_data = {'dose': []}

	for i in range(0, len(cum_dist)):
		json_data['dose'].append([bin_centers[i], cum_dist[i]])

	return json_data


