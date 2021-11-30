from django.urls import path

from .views import download_all_rows_view

urlpatterns = [
    path('all-rows/<uuid:pk>/', download_all_rows_view, name='texfiles_download_all_rows_url')
]
