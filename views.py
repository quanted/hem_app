from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.conf import settings
from .forms import RunForm
from .models import Category, Chemical, Person, RunHistory, Dose
from django.utils import timezone
from djqscsv import render_to_csv_response
from .analysis_funcs import get_chemical_data
import pandas as pd


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
	#TODO Logic for products and chemicals -> only chemical now
	chemical = rh.chemical_id
	plot_data = get_chemical_data(chemical)
	c = Chemical.objects.get(pk=chemical)
	chem = {'name': c.title, 'cas': c.cas}
	html = render_to_string('hem_results.html')
	response = HttpResponse()
	response.write(html)
	return render(request, 'hem_results.html', {'pfile_name': pfile_name, 'dfile_name': dfile_name,
												'run_history_id': run_history_id, 'plot_data': plot_data,
												'chem': chem, 'rh': rh})

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


def hem_index(request):
	form = RunForm()
	if request.method =="POST":
		form = RunForm(request.POST)
		if form.is_valid():
			categories = Category.objects.get(pk=request.POST.get('selectProduct'))
			products = request.POST.get('inlineRadioOptions')
			history = form.save(commit=False)
			history.created_at = timezone.now()
			history.updated_at = timezone.now()
			history.categories = categories
			history.products = products
			history.save()

			# send the runHistory id to the results page via a session
			request.session['run_history_id'] = history.id

			return HttpResponseRedirect('results', {'runHistory': history})

	return render(request, 'hem_index.html', {'form': form})

