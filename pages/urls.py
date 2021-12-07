from django.urls import path

from .views import landing_page_view, privacy_policy_view, terms_of_service_view

urlpatterns = [
    path('', landing_page_view, name='landing_page_url'),
    path('', privacy_policy_view, name='privacy_policy_url'),
    path('', terms_of_service_view, name='terms_of_service_url'),
]
