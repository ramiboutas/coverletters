from django.urls import path, include
from .views import CoverLetterListView, CoverLetterDetailView, CoverLetterCreateView,CoverLetterUpdateView
from .views import hx_save_text_first_time_view, hx_save_text_dynamic_view
from .views import hx_add_row_view, hx_add_table_column_view
from .views import hx_save_hashtag_view





urlpatterns = [
    path('', CoverLetterListView.as_view(), name='coverletters_list'),
    path('detail/<int:pk>/', CoverLetterDetailView.as_view(), name='coverletters_detail'),
    path('update/<int:pk>/', CoverLetterUpdateView.as_view(), name='coverletters_update'),
    path('new/', CoverLetterCreateView.as_view(), name='coverletters_new'),

    # htmx - text - create and save (coverletter.save_text_dynamic_url)
    path('hx-text-save-create-object/', hx_save_text_first_time_view, name='coverletters_hx_save_text_first_time_url'),
    path('hx-text-save/<int:pk>/', hx_save_text_dynamic_view, name='coverletters_hx_save_text_dynamic_url'),

    # htmx - table - row (coverletter.add_table_row_url)
    path('hx-table-add-row/<int:pk>/', hx_add_row_view, name='coverletters_hx_add_row_url'),

    # htmx - table - column (coverletter.add_table_row_url)
    path('hx-table-add-hashtag-column/<int:pk>/', hx_add_table_column_view, name='coverletters_hx_add_table_column_url'),

    # htmx - table - save hashtag (hashtag.save_url)
    path('hx-table-save-hashtag/<int:pk_parent>/<int:pk>/', hx_save_hashtag_view, name='coverletters_hx_save_hashtag_url'),


]
