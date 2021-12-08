from django.urls import path, include
from .views import CoverLetterListView, CoverLetterCreateView,CoverLetterUpdateView
from .views import hx_create_object_view
from .views import hx_delete_object_view 
from .views import hx_save_text_dynamic_view
from .views import hx_save_company_text_dynamic_view
from .views import hx_save_candidate_info_dynamic_view
from .views import hx_save_applying_position_dynamic_view
from .views import hx_save_location_date_dynamic_view
from .views import hx_add_table_row_view, hx_add_table_column_view
from .views import hx_delete_table_column_view, hx_delete_table_row_view
from .views import hx_save_hashtag_view
from .views import hx_get_or_create_item_view


urlpatterns = [

    path('my-coverletters/', CoverLetterListView.as_view(), name='coverletters_list'),
    path('new/', CoverLetterCreateView.as_view(), name='coverletters_new'),
    # path('detail/<int:pk>/', CoverLetterDetailView.as_view(), name='coverletters_detail'),
    path('coverletter/<uuid:pk>/', CoverLetterUpdateView.as_view(), name='coverletters_update'),

    # htmx - object (coverletter) - delete
    path('hx-delete-coverletter/<uuid:pk>/', hx_delete_object_view, name='coverletters_delete'),

    # htmx - object (coverletter) - create
    path('hx-text-create-object/', hx_create_object_view, name='coverletters_hx_create_object_url'),

    # htmx - text - save (coverletter.save_text_dynamic_url)
    path('hx-text-save/<uuid:pk>/', hx_save_text_dynamic_view, name='coverletters_hx_save_text_dynamic_url'),

    # htmx - company_text -  save (coverletter.save_company_text_dynamic_url)
    path('hx-company-text-save/<uuid:pk>/', hx_save_company_text_dynamic_view, name='coverletters_hx_save_company_text_dynamic_url'),

    # htmx - applying_position -  save (coverletter.save_applying_position_dynamic_url)
    path('hx-applying-position-save/<uuid:pk>/', hx_save_applying_position_dynamic_view, name='coverletters_hx_save_applying_position_dynamic_url'),

    path('hx-candidate-info-save/<uuid:pk>/', hx_save_candidate_info_dynamic_view, name='coverletters_hx_save_candidate_info_dynamic_url'),

    path('hx-location-date-save/<uuid:pk>/', hx_save_location_date_dynamic_view, name='coverletters_hx_save_location_date_dynamic_url'),

    # htmx - table - row (coverletter.add_table_row_url)
    path('hx-table-add-row/<uuid:pk>/', hx_add_table_row_view, name='coverletters_hx_add_table_row_url'),

    # htmx - table - column (coverletter.add_table_row_url)
    path('hx-table-add-hashtag-column/<uuid:pk>/', hx_add_table_column_view, name='coverletters_hx_add_table_column_url'),

    # htmx - table - save hashtag (hashtag.save_url)
    path('hx-table-save-hashtag/<int:pk>/<int:pk_column>/', hx_save_hashtag_view, name='coverletters_hx_save_hashtag_url'),

    # htmx - table - delete column (column.delete_url)
    path('hx-table-delete-column/<int:pk>/<uuid:pk_parent>/', hx_delete_table_column_view, name='coverletters_hx_delete_table_column_url'),

    # htmx - table - delete column (column.delete_url)
    path('hx-table-delete-row/<int:pk>/<uuid:pk_parent>/', hx_delete_table_row_view, name='coverletters_hx_delete_table_row_url'),

    # htmx - table - create item
    path('hx-table-create-item/<int:pk_row>/<int:pk_column>/', hx_get_or_create_item_view, name='coverletters_hx_get_or_create_item_url'),


]
