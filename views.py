from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.conf import settings
from .forms import RunForm
from .models import Category, Chemical, Person, RunHistory
from django.utils import timezone
from djqscsv import render_to_csv_response

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
    file_name = 'population_' + str(run_history_id)
    html = render_to_string('hem_results.html')
    response = HttpResponse()
    response.write(html)
    return render(request, 'hem_results.html', {'file_name': file_name, 'run_history_id': run_history_id})

def hem_results_population_csv(request):
	run_history_id = request.session.get('run_history_id')
	qs = get_population_qs(run_history_id)
	file_name = 'population_' + str(run_history_id)
	return render_to_csv_response(qs, file_name)


def hem_index(request):
	form = RunForm()
	if request.method =="POST":
		form = RunForm(request.POST)
        if form.is_valid():
            chemical = Chemical.objects.get(pk=request.POST.get('selectChemical'))
            categories = Category.objects.get(pk=request.POST.get('selectProduct'))
            products = request.POST.get('inlineRadioOptions')
            history = form.save(commit=False)
            history.created_at = timezone.now()
            history.updated_at = timezone.now()
            history.chemical = chemical
            history.categories = categories
            history.products = products
            history.save()

            # send the runHistory id to the results page via a session
            request.session['run_history_id'] = history.id

            return HttpResponseRedirect('results', {'runHistory': history})
    
        return render(request, 'hem_index.html', {'form': form})
