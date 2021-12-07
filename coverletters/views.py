from django_htmx.http import trigger_client_event

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve, reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from utils.sessions import create_or_get_session_object
from .models import CoverLetter, Hashtag, Item, Row, Column



class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect']=self['Location']
    status_code = 200


class CoverLetterUpdateView(UpdateView):
    template_name = 'coverletter_form.html'
    model = CoverLetter
    fields = '__all__'
    # exclude = ['candidate_name','candidate_position','candidate_email', 'candidate_phone','candidate_location', 'candidate_website']
    def get_object(self):
        session, self.request = create_or_get_session_object(self.request)
        obj = get_object_or_404(CoverLetter, pk=self.kwargs['pk'], session=session)
        return obj


class CoverLetterListView(ListView):
    template_name = 'coverletter_list.html'
    model = CoverLetter

    def get_queryset(self):
        queryset = super(CoverLetterListView, self).get_queryset()
        session, self.request = create_or_get_session_object(self.request)
        queryset = queryset.filter(session=session)
        return queryset

class CoverLetterCreateView(CreateView):
    template_name = 'coverletter_form.html'
    model = CoverLetter
    fields = '__all__'
    # exclude = ['candidate_name','candidate_position','candidate_email', 'candidate_phone','candidate_location', 'candidate_website']
    def form_valid(self, form):
        # as the user goes to the create view,
        # we create the object directly with the predefined text in the textarea
        response = super(CoverLetterCreateView, self).form_valid(form)
        trigger_client_event(response, 'ObjectCreatedEvent', { },)
        return response


# htmx - coverletter - create object
@require_POST
def hx_create_object_view(request):
    session_object, request = create_or_get_session_object(request)
    text = request.POST.get("text")
    company_text = request.POST.get("company_text")
    location_date = request.POST.get("location_date")
    applying_position = request.POST.get("applying_position")
    object = CoverLetter(session=session_object, text=text, company_text=company_text, location_date=location_date, applying_position=applying_position)
    object.save()
    # once the object is created, we redirect the user to the obj update url
    return HTTPResponseHXRedirect(redirect_to=object.get_update_url())

# htmx - (body) text - save
@require_POST
def hx_save_text_dynamic_view(request, pk=None):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    text = request.POST.get("text")
    object.text = text
    object.save()
    return HttpResponse(status=200)

# htmx - company text - save

def hx_save_company_text_dynamic_view(request, pk=None):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    company_text = request.POST.get("company_text")
    object.company_text = company_text
    object.save()
    return HttpResponse(status=200)

# htmx - applying position - save
@require_POST
def hx_save_applying_position_dynamic_view(request, pk=None):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    applying_position = request.POST.get("applying_position")
    object.applying_position = applying_position
    object.save()
    return HttpResponse(status=200)


# htmx - candidate info - save
@require_POST
def hx_save_candidate_info_dynamic_view(request, pk=None):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    candidate_name = request.POST.get("candidate_name")
    candidate_position = request.POST.get("candidate_position")
    candidate_email = request.POST.get("candidate_email")
    candidate_phone = request.POST.get("candidate_phone")
    candidate_location = request.POST.get("candidate_location")
    candidate_website = request.POST.get("candidate_website")
    object.candidate_name = candidate_name
    object.candidate_position = candidate_position
    object.candidate_email = candidate_email
    object.candidate_phone = candidate_phone
    object.candidate_location = candidate_location
    object.candidate_website = candidate_website
    object.save()
    return HttpResponse(status=200)

def hx_save_location_date_dynamic_view(request, pk=None):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    location_date = request.POST.get("location_date")
    object.location_date = location_date
    object.save()
    return HttpResponse(status=200)


# htmx - table - add row
MAX_NUMBER_OF_ROWS=50 # in case the default from the db does not work
def hx_add_table_row_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    rows_count = object.rows.count()
    if rows_count < MAX_NUMBER_OF_ROWS:
        row = Row.objects.create(coverletter=object)
        context = {'object': object, 'row': row, 'current_row_number': rows_count+1}
        return render(request, 'partials/table_new_row.html', context)
    else:
        # message danger
        return HttpResponse()

# htmx - table - add column
def hx_add_table_column_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    column = Column(coverletter=object)
    column.save()
    hashtag = Hashtag(column=column, name='#new')
    hashtag.save()
    context = {'object': object}
    return render(request, 'partials/table.html', context)

# htmx -  table - delete column
@require_POST
def hx_delete_table_column_view(request, pk, pk_parent):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk_parent, session=session_object)
    column = get_object_or_404(Column, pk=pk, coverletter=object)
    column.delete()
    context = {'object': object}
    return render(request, 'partials/table.html', context)

# htmx - table - delete row
@require_POST
def hx_delete_table_row_view(request, pk, pk_parent):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk_parent, session=session_object)
    row = get_object_or_404(Row, pk=pk, coverletter=object)
    row.delete()
    context = {'object': object}
    return render(request, 'partials/table.html', context)


# htmx - table - save hashtag
@require_POST
def hx_save_hashtag_view(request, pk, pk_column):
    name = request.POST.get(f"hashtag_{pk}")
    if name =="": name = "#"    # if user leaves the field empty -> we add a "#" character
    hashtag = get_object_or_404(Hashtag, column__pk=pk_column, pk=pk)
    hashtag.name = name
    hashtag.save()
    return render(request, 'partials/table_hashtag_form_input.html', {'hashtag': hashtag})


# htmx - table - save item
@require_POST
def hx_get_or_create_item_view(request, pk_row, pk_column ):
    item_name = request.POST.get(f"item_{pk_row}_{pk_column}")
    row = get_object_or_404(Row, pk=pk_row)
    column = get_object_or_404(Column, pk=pk_column)
    try:
        item = Item.objects.get(row=row, column=column)
    except ObjectDoesNotExist:
        item = Item.objects.create(row=row, column=column)
    item.name=item_name
    item.save()
    return HttpResponse(status=200)
    # context = {'row': row, 'column': column, 'item': item }
    # return render(request, 'partials/table_item_form_input.html', context)
