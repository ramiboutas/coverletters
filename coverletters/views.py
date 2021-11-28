from django_htmx.http import trigger_client_event

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve, reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import CoverLetter, Hashtag, Item, Row, Column

class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect']=self['Location']
    status_code = 200


class CoverLetterListView(ListView):
    model = CoverLetter


class CoverLetterDetailView(DetailView):
    model = CoverLetter

class CoverLetterUpdateView(UpdateView):
    model = CoverLetter
    fields = ['text']

class CoverLetterCreateView(CreateView):
    model = CoverLetter
    fields = ['text']
    def form_valid(self, form):
        # as the user goes to the create view,
        # we create the object directly with the predefined text in the textarea
        response = super(CoverLetterCreateView, self).form_valid(form)
        trigger_client_event(response, 'ObjectCreatedEvent', { },)
        return response


# htmx - saving text

@require_POST
def hx_save_text_first_time_view(request):
    text = request.POST.get("text")
    object = CoverLetter(text=text)
    object.save()
    # once the object is created, we redirect the user to the obj update url
    return HTTPResponseHXRedirect(redirect_to=object.get_update_url())


@require_POST
def hx_save_text_dynamic_view(request, pk=None):
    text = request.POST.get("text")
    object = get_object_or_404(CoverLetter, pk=pk)
    object.text = text
    object.save()
    return HttpResponse(status=200)



# htmx - table - add row
MAX_NUMBER_OF_ROWS=50
def hx_add_table_row_view(request, pk):
    object = get_object_or_404(CoverLetter, pk=pk)
    rows_count = object.rows.count()
    if rows_count < MAX_NUMBER_OF_ROWS:
        row = Row.objects.create(coverletter=object)
        context = {'object': object, 'row': row}
        return render(request, 'coverletters/partials/table_new_row.html', context)
    else:
        return HttpResponse()



# htmx - table - add column
def hx_add_table_column_view(request, pk):
    object = get_object_or_404(CoverLetter, pk=pk)
    column = Column(coverletter=object)
    column.save()
    hashtag = Hashtag(column=column, name='#new')
    hashtag.save()
    context = {'object': object}
    return render(request, 'coverletters/partials/table.html', context)


# htmx - save hashtag
@require_POST
def hx_save_hashtag_view(request, pk, pk_column):
    name = request.POST.get(f"hashtag_{pk}")
    if name =="": name = "#"    # if user leaves the field empty -> we add a "#" character
    hashtag = get_object_or_404(Hashtag, column__pk=pk_column, pk=pk)
    hashtag.name = name
    hashtag.save()
    return render(request, 'coverletters/partials/hashtag_form_input.html', {'hashtag': hashtag})


# htmx - save item
@require_POST
def hx_create_item_view(request, pk_row, pk_column ):
    item_name = request.POST.get(f"item_{pk_row}_{pk_column}")
    row = get_object_or_404(Row, pk=pk_row)
    column = get_object_or_404(Column, pk=pk_column)
    item = Item.objects.create(row=row, column=column, name=item_name)
    context = {'row': row, 'column': column, 'item': item }
    return render(request, 'coverletters/partials/item_form_input.html', context)


# temporal view - get item
# def hx_get_item_view(request, pk_parent, row_position):
#     item_name = request.GET.get(f"item_{pk_parent}_{row_position}")
#     hashtag = get_object_or_404(Hashtag, pk=pk_parent)
#     item = Item(hashtag=hashtag, name=item_name, row_position=row_position)
#     item.save()
#     context = {'hashtag': hashtag, 'item': item , 'row_position': row_position}
#     return render(request, 'coverletters/partials/item_form_input.html', context)


# htmx - save item
@require_POST
def hx_save_item_view(request, pk_parent, pk):
    # pk_parent -> hashtag.pk
    # item -> item.pk
    pass
