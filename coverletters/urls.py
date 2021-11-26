from django.urls import path, include
from .views import CoverLetterListView, CoverLetterDetailView, CoverLetterCreateView,CoverLetterUpdateView
from .views import hx_first_save_view, hx_dynamic_save_view
from .views import hx_add_row_view, hx_add_body_column_view, hx_add_head_column_view
from .views import hx_fire_column_change_event_view
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
    path('hx-table-add-row/', hx_add_row_view, name='coverletters_hx_add_row_url'),
    path('hx-table-fire-column-change-event/', hx_fire_column_change_event_view, name='coverletters_hx_fire_column_change_event_url'),
    path('hx-table-add-body-column/', hx_add_body_column_view, name='coverletters_hx_add_body_column_url'),
    path('hx-table-add-head-column/', hx_add_head_column_view, name='coverletters_hx_add_head_column_url'),

    # htmx - table saving
    path('hx-table-save-data/<int:pk>/', hx_save_table_data_view, name='coverletters_hx_save_table_data_url'),


]
