from django.urls import path

from .views import prepare_the_download_view, download_the_zip_file_view, hx_get_buy_me_a_coffee_partial_view

urlpatterns = [
    path('prepare-the-download/<uuid:pk>/', prepare_the_download_view, name='texfiles_prepare_the_download_url'),
    path('get-zip-file/<uuid:pk>/', download_the_zip_file_view, name='texfiles_download_the_zip_file_url'),
    path('get-buy-me-a-coffee-partial', hx_get_buy_me_a_coffee_partial_view, name='hx_get_buy_me_a_coffee_partial_url'),

]
