from hem_app.models import Dose, Category, RunParams
import pandas as pd


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

	population_null = 80

	# Magic from Katherine Phillips
	data = data[['id', 'day', 'dir_derm_abs', 'dir_ingest_abs', 'dir_inhal_abs']].copy()
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


