from django.urls import path, include
from .views import CoverLetterListView, CoverLetterDetailView, CoverLetterCreateView,CoverLetterUpdateView
from .views import hx_first_save_view, hx_dynamic_save_view
from .views import hx_add_row_view
from .views import hx_add_table_hashtag_view
from .views import hx_reached_max_of_hashtags_view
from .views import hx_save_table_data_view



urlpatterns = [
    path('', CoverLetterListView.as_view(), name='coverletters_list'),
    path('detail/<int:pk>/', CoverLetterDetailView.as_view(), name='coverletters_detail'),
    path('update/<int:pk>/', CoverLetterUpdateView.as_view(), name='coverletters_update'),
    path('new/', CoverLetterCreateView.as_view(), name='coverletters_new'),

    # htmx - saving text
    path('hx-text-save/', hx_first_save_view, name='coverletters_hx_first_save_url'),
    path('hx-text-save/<int:pk>/', hx_dynamic_save_view, name='coverletters_hx_dynamic_save_url'),

    # htmx - table manipulation
    path('hx-table-add-row/<int:pk>/', hx_add_row_view, name='coverletters_hx_add_row_url'),
    path('hx-table-add-hashtag/<int:pk>/', hx_add_table_hashtag_view, name='coverletters_hx_add_table_hashtag_url'),

    path('hx-table-max-hashtags-reached/', hx_reached_max_of_hashtags_view, name='coverletters_hx_reached_max_of_hashtags_url'),

    # htmx - table saving
    path('hx-table-save-data/<int:pk>/', hx_save_table_data_view, name='coverletters_hx_save_table_data_url'),


]
