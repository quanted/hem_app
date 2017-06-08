from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.conf import settings
from .forms import RunForm
from .models import Product, Chemical, RunHistory
from django.utils import timezone
from djqscsv import render_to_csv_response
from .analysis_funcs import get_chemical_data, get_dose_qs, get_population_qs, get_lcia_qs


def hem_landing_page(request):
	""" Returns the html of the landing page for qed. """
	html = render_to_string('01epa_drupal_header.html', {})
	html += render_to_string('02epa_drupal_header_bluestripe.html', {})
	html += render_to_string('03epa_drupal_section_title.html', {})
	if settings.IS_PUBLIC:
		html += render_to_string('hem_popgen.html', {'title': 'Human Exposure Model'})
		pass
	else:
		html += render_to_string('hem_popgen.html', {'title': 'Human Exposure Model'})
		pass
	html += render_to_string('09epa_drupal_splashscripts.html', {})
	html += render_to_string('10epa_drupal_footer.html', {})
	response = HttpResponse()
	response.write(html)
	return response

def file_not_found(request):
	""" Returns the html of the landing page for qed. """
	html = render_to_string('01epa_drupal_header.html', {})
	html += render_to_string('02epa_drupal_header_bluestripe.html', {})
	html += render_to_string('03epa_drupal_section_title.html', {})
	if settings.IS_PUBLIC:
		html += render_to_string('04qed_splash_landing_public.html', {'title': 'qed'})
	else:
		html += render_to_string('04qed_splash_landing_intranet.html', {'title': 'qed'})
	html += render_to_string('09epa_drupal_splashscripts.html', {})
	html += render_to_string('10epa_drupal_footer.html', {})
	response = HttpResponse()
	response.write(html)
	return response

def hem_results(request):
	""" Landing page for results of model run """
	run_history_id = request.session.get('run_history_id')
	rh = RunHistory.objects.get(pk=int(run_history_id))

	pfile_name = 'population_' + str(run_history_id)
	dfile_name = 'dose_' + str(run_history_id)
	colors = ['rgba(119, 152, 191, .5)', 'rgba(141, 211, 199, .5)', 'rgba(150, 255, 179, .7)',
			  'rgba(190, 186, 218, .5)', 'rgba(251, 128, 114, .5)', 'rgba(128, 177, 211, .5)',
			  'rgba(253, 180, 98, .5)', 'rgba(179, 222, 105, .5)', 'rgba(252, 205, 229, .5)',
			  'rgba(217, 217, 217, .5)', 'rgba(188, 128, 189, .5)', 'rgba(204, 235, 197, .5)',
			  'rgba(255, 237, 111, .5)']

	#TODO Logic for products and chemicals -> only chemical now
	if rh.is_product == 0:
		chemical = rh.chemical_id
		plot_data = get_chemical_data(chemical)
		c = Chemical.objects.get(pk=chemical)
		chem = [{'name': c.title, 'cas': c.cas, 'dtxsid': c.dtxsid, 'plot_data': plot_data,
				 'plot_color': colors[0]}]
	else:
		print("put multichems here")

	products = Product.objects.get(pk=rh.product_id)

	html = render_to_string('hem_results.html')
	response = HttpResponse()
	response.write(html)
	return render(request, 'hem_results.html', {'pfile_name': pfile_name, 'dfile_name': dfile_name,
												'run_history_id': run_history_id, 'chem': chem, 'rh': rh,
												'products': products})

def hem_results_population_csv(request):
	run_history_id = request.session.get('run_history_id')
	qs = get_population_qs(run_history_id)
	file_name = 'population_' + str(run_history_id)
	return render_to_csv_response(qs, file_name)

def hem_results_dose_csv(request):
	run_history_id = request.session.get('run_history_id')
	qs = get_dose_qs(run_history_id)
	file_name = 'dose_' + str(run_history_id)
	return render_to_csv_response(qs, file_name)

def hem_results_lcia_csv(request):
	run_history_id = request.session.get('run_history_id')
	qs = get_lcia_qs(run_history_id)
	file_name = 'lcia_' + str(run_history_id)
	return render_to_csv_response(qs, file_name)


def hem_index(request):
	form = RunForm()
	if request.method =="POST":
		form = RunForm(request.POST)
		if form.is_valid():
			products = request.POST.get('inlineRadioOptions')
			history = form.save(commit=False)
			history.created_at = timezone.now()
			history.updated_at = timezone.now()
			history.is_product = products
			history.save()

			# send the runHistory id to the results page via a session
			request.session['run_history_id'] = history.id

			return HttpResponseRedirect('results', {'runHistory': history})

	return render(request, 'hem_index.html', {'form': form})

