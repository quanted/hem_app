from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
#import links_left
import os, tempfile, zipfile
#import secret
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
from .forms import HemForm


def send_file(request):
    filename = "../static_qed/hem/files/example.csv"  # Select your file here.
    download_name = "example.csv"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=%s" % download_name
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

    if request.method == 'POST':
        form = HemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect('hem_results')
    else:
        form = HemForm()
        return render(request, 'hem_popgen.html', {'form': form})


def hem_results(request):
    html = render_to_string('hem_results.html', {})
    response = HttpResponse()
    response.write(html)
    return response
