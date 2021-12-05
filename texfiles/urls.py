from django.urls import path

from .views import prepare_the_download_view, download_the_zip_file_view

urlpatterns = [
    path('prepare-the-download/<uuid:pk>/', prepare_the_download_view, name='texfiles_prepare_the_download_url'),
    path('get-zip-file/<uuid:pk>/', download_the_zip_file_view, name='texfiles_download_the_zip_file_url'),
]
