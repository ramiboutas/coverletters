from django_htmx.http import trigger_client_event

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import CoverLetter

class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect']=self['Location']
    status_code = 200


class CoverLetterListView(ListView):
    model = CoverLetter

class CoverLetterCreateView(CreateView):
    model = CoverLetter
    fields = ['text']

class CoverLetterDetailView(DetailView):
    model = CoverLetter

class CoverLetterUpdateView(UpdateView):
    model = CoverLetter
    fields = ['text']


# htmx - saving text

@require_POST
def hx_first_save_view(request):
    text = request.POST.get("text")
    object = CoverLetter(text=text)
    object.save()
    return HTTPResponseHXRedirect(redirect_to=object.get_update_url())


@require_POST
def hx_dynamic_save_view(request, pk=None):
    text = request.POST.get("text")
    object = get_object_or_404(CoverLetter, pk=pk)
    object.text = text
    object.save()
    return HttpResponse(status=200)

# htmx - table

def hx_add_row_view(request):
    return render(request, 'coverletters/partials/table_new_row.html')



def hx_fire_column_change_event_view(request):
    response = HttpResponse()
    trigger_client_event(response, 'ColumnsChangedEvent', { },)
    return response



def hx_add_body_column_view(request):
    return render(request, 'coverletters/partials/table_new_body_td.html')


def hx_add_head_column_view(request):
    return render(request, 'coverletters/partials/table_new_head_th.html')
