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
from .models import Category, RunHistory, Dose, Chemical
# from rest_framework.views import APIView
# from rest_framework.response import Response
from dal import autocomplete
from django.utils import timezone

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


def hem_popgen(request):
    """ Main landing and form for hem_app """
    all_categories = Category.objects.filter(parent=None).values_list('id', 'title')
    pform = ProductForm(request.POST)
    if request.method == 'POST':
        if pform.is_valid():
            sub_category = request.POST.get('sub_category', -1)
            category = Category.objects.get(id=sub_category) #form.cleaned_data['sub_category1'])
            product= request.POST.get('toggleProducts', True)
            population_size = form.cleaned_data.get('population_field')
            gender = request.POST['optionsRadiosGender']
            age_radio = request.POST['optionsRadiosAge']
            min_age = 0
            mix_age = 0
            if age_radio == 'age1':
                min_age = 0
                mix_age = 5
            elif age_radio == 'age2':
                min_age = 6
                mix_age = 12
            elif age_radio == 'age3':
                min_age = 13
                mix_age = 15
            elif age_radio == 'age4':
                min_age = 16
                mix_age = 18
            elif age_radio == 'age5':
                min_age = 19
                mix_age = 49
            elif age_radio == 'age6':
                min_age = 49
                mix_age = 99
            history = RunHistory(categories=category, products=product, population_size=population_size,
                                 gender=gender, min_age=min_age, max_age=mix_age)
            history.save()
            return HttpResponseRedirect('results',  {'all_historyRows': all_categories})
        else: raise Http404('Unable to save population generation data..')
    else:
           return render(request, 'hem_popgen.html', {'form': pform, 'all_categories': all_categories })


def hem_results(request):
    """ Landing page for results of model run """
    all_history = RunHistory.objects.all()
    html = render_to_string('hem_results.html', {'all_history': all_history})
    response = HttpResponse()
    response.write(html)
    return response

def hem_index(request):
	form = RunForm()
	if request.method =="POST":
		form = RunForm(request.POST)
        if form.is_valid():
	        population_size = form.cleaned_data.get('population_field')
	        history.population_size = population_size
	        history = form.save(commit=False)
	        history.chemical_id = 1
	        history.categories_id = 1
	        history.created_at = timezone.now()
	        history.updated_at = timezone.now()
	        history.save()
	        return HttpResponseRedirect('results')

	return render(request, 'hem_index.html', {'form': form})


def get_json_data(request):
    #data1 = [data.gender and data.population_size  for data in RunHistory.objects.all()]
    data = dict(history=list(RunHistory.objects.values('gender', 'population_size', 'min_age', 'max_age', 'categories_id')))
    return JsonResponse(data, safe=True)


def query_category(request):
    parent_id = request.GET.get('care_id', None)
    data = list(Category.objects.filter(parent_id=parent_id).values('id', 'title'))  #.values_list('id', 'title'))
    return JsonResponse({'care_id': data }, content_type="application/json", safe=True)


class ChemicalAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		data = Chemical.objects.exclude(dose=None)

		if self.q:
			data = data.filter(cas__istartswith=self.q)

		return data
