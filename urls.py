#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import url
from . import views

app_name = 'hem_app'

if settings.IS_PUBLIC:
    urlpatterns = [
        #url(r'^api/', include('api.urls')),
        #url(r'^rest/', include('REST.urls')),
        url(r'^$', views.hem_landing_page),
        url(r'^index/?$', views.hem_index),
        url(r'^hem_jdata/$', views.get_json_data),
        url(r'^category_list/$', views.query_category),
        #url(r'^hem_data/?$', views.get_results.as_view()),
        url(r'^results/?$', views.hem_results),
        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]
else:
    urlpatterns = [
        #url(r'^api/', include('api.urls')),
        #url(r'^rest/', include('REST.urls')),
        url(r'^$', views.hem_landing_page),
        url(r'^index/?$', views.hem_index),
        url(r'^hem_jdata/$', views.get_json_data),
        url(r'^category_list/$', views.query_category),
        #url(r'^hem_data/?$', views.get_results.as_view()),
        url(r'^results/?$', views.hem_results),
        # url(r'^$', views.qed_splash_page_intrane
        #url(r'^$', views.qed_splash_page_intranet),
        # url(r'^admin/', include(admin.site.urls)),
    ]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found
