from django_tex.shortcuts import render_to_pdf
from django.shortcuts import render

from .models import TexFile

def download_all_rows_view(request, pk):
    texfile_pk = int(request.POST.get("texfileselected_pk"))
    texfile_obj = TexFile.objects.get(pk=texfile_pk)
    template_name = texfile_obj.file.path
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')
