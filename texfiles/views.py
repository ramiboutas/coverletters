from django_tex.shortcuts import render_to_pdf
from django.shortcuts import render

# Create your views here.


def download_all_view(request):
    template_name = 'test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')
