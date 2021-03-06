#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'hem_app'

if settings.IS_PUBLIC:
    urlpatterns = [
        # #url(r'^api/', include('api.urls')),
        # #url(r'^rest/', include('REST.urls')),
        # url(r'^$', views.hem_landing_page),
        # url(r'^index/?$', views.hem_index),
        # url(r'^results/?$', views.hem_results),
        # url(r'^about/?$', views.hem_about),
        # # url(r'^admin/', include(admin.site.urls)),
        path('', views.hem_landing_page),
        path('index/', views.hem_index),
        path('results/', views.hem_results),
        path('about/', views.hem_about),
    ]
else:
    urlpatterns = [
        # #url(r'^api/', include('api.urls')),
        # #url(r'^$', views.qed_splash_page_intranet),
        # #url(r'^rest/', include('REST.urls')),
        # url(r'^$', views.hem_landing_page),
        # url(r'^index/?$', views.hem_index),
        # url(r'^results/?$', views.hem_results),
        # url(r'^about/?$', views.hem_about),
        # # url(r'^$', views.qed_splash_page_intrane
        # #url(r'^$', views.qed_splash_page_intranet),
        # # url(r'^admin/', include(admin.site.urls)),

        path('', views.hem_landing_page),
        path('index/', views.hem_index),
        path('results/', views.hem_results),
        path('about/', views.hem_about),
    ]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found

