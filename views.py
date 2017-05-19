from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, render_to_response, redirect
import os
import tempfile
import zipfile
import json
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
from .forms import RunForm
from .models import Category, RunHistory, Dose, Chemical, Person
# from rest_framework.views import APIView
# from rest_framework.response import Response
from dal import autocomplete
from django.utils import timezone
from djqscsv import write_csv, render_to_csv_response

def send_file(request):
    """ returns a static file for testing """
    filename = "../static_qed/hem/files/example.csv"  # Select your file here.
    download_name = "example.csv"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename={0!s}".format(download_name)
    return response


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
    html = render_to_string('hem_results.html')
    response = HttpResponse()
    response.write(html)
    return response

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
            #create the queryset for population csv - should include gender and ages
            if history.gender == 'B':
                pop_qs = Person.objects.filter(age_years__gte=history.min_age,
                                               age_years__lte=history.max_age).values('id', 'gender', 'race',
                                                                                      'ethnicity', 'age_years', 'ages',
                                                                                      'genders', 'baths', 'lot',
                                                                                      'dishwash', 'cwasher', 'swim')

            else:
                pop_qs = Person.objects.filter(gender=history.gender, age_years__gte=history.min_age,
                                               age_years__lte=history.max_age).values('id', 'gender', 'race',
                                                                                     'ethnicity', 'age_years', 'ages',
                                                                                     'genders', 'baths', 'lot',
                                                                                     'dishwash', 'cwasher', 'swim')

            # name the population csv
            csvName = 'static_qed/hem/files/population_' + str(history.id) + '.csv'
            with open(csvName, 'wb') as csv_file:
                write_csv(pop_qs, csv_file)
                print(csv_file)

            return HttpResponseRedirect('results', {'runHistory': history})
    
        return render(request, 'hem_index.html', {'form': form})
