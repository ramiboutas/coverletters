from django.urls import path, include
from .views import (CoverLetterListView, CoverLetterDetailView, CoverLetterCreateView,CoverLetterUpdateView,
                    hx_first_save_view, hx_dynamic_save_view,
                    hx_add_row_view, hx_add_body_column_view)

urlpatterns = [
    path('', CoverLetterListView.as_view(), name='coverletters_list'),
    path('<int:pk>/', CoverLetterDetailView.as_view(), name='coverletters_detail'),
    path('<int:pk>/update/', CoverLetterUpdateView.as_view(), name='coverletters_update'),
    path('new/', CoverLetterCreateView.as_view(), name='coverletters_new'),

    # htmx - saving text
    path('hx-text-save/', hx_first_save_view, name='coverletters_hx_first_save_url'),
    path('hx-text-save/<int:pk>/', hx_dynamic_save_view, name='coverletters_hx_dynamic_save_url'),
    # htmx - table
    path('hx-table-add-row/', hx_add_row_view, name='coverletters_hx_add_row_url'),
    path('hx-table-add-body-column/', hx_add_body_column_view, name='coverletters_hx_add_body_column_url'),


]
