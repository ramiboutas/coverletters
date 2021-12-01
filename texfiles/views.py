from pathlib import Path
from django_tex.shortcuts import render_to_pdf

from django.shortcuts import render
from django.conf import settings
from .models import TexFile

# settings.MEDIA_ROOT = /mnt/c/Users/rboutass/Documents/python_stuff/django-stuff/cover-letters/texfiles/templates
# template_name_abs = /mnt/c/Users/rboutass/Documents/python_stuff/django-stuff/cover-letters/texfiles/templates/texfiles/file4.tex/

def _get_tex_template_name(file_obj):
    template_name_abs = Path(file_obj.file.path)
    media_path_abs = settings.MEDIA_ROOT
    template_name_rel = template_name_abs.relative_to(media_path_abs)
    print(f'settings.MEDIA_ROOT = {settings.MEDIA_ROOT}')
    print(f'template_name_abs = {template_name_abs}')
    print(f'template_name_rel = {template_name_rel}')
    return str(template_name_rel)


def download_all_rows_view(request, pk):
    texfile_pk = int(request.POST.get("texfileselected_pk"))
    texfile_obj = TexFile.objects.get(pk=texfile_pk)
    template_name = _get_tex_template_name(texfile_obj)
    # template_name = "texfiles/file2.tex"
    print(template_name)
    context = {'text': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')

def download_a_certain_row_view(request, pk, pk_row):
    pass
