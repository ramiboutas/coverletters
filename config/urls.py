"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.http import FileResponse

def awful_function_to_send_a_file(request, dir_path, file_path):
    file = open(f"media/{dir_path}/{file_path}", 'rb')
    response = FileResponse(file)
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('pages.urls')),
    path('coverletters/', include('coverletters.urls')),
    path('templates/', include('texfiles.urls')),
    re_path(r'^celery-progress/', include('celery_progress.urls')),
    path('media/<str:dir_path>/<str:file_path>/', awful_function_to_send_a_file),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # it does not work...
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(re_path(r'^rosetta/', include('rosetta.urls')))