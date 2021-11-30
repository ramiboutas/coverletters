from django.urls import path

from .views import download_all_view

urlpatterns = [
    path('all', download_all_view, name='texfiles_download_all_url')
]
