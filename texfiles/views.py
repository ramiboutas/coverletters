from pathlib import Path
from django_tex.shortcuts import render_to_pdf
from django_tex.core import compile_template_to_pdf

from django.shortcuts import render
from django.conf import settings
from .models import TexFile


def get_tex_template_name(file_obj):
    template_name_abs = Path(file_obj.file.path)
    template_name_rel = template_name_abs.relative_to(settings.MEDIA_ROOT)
    return str(template_name_rel)


# https://www.py4u.net/discuss/1262171
# extM3u = str.encode(body.decode('utf8').split('EXTM3U
# #')[1].split('------WebKitFormBoundary')[0])
# fileTemp = NamedTemporaryFile(delete=True, dir='media/tmp')
# fileTemp.write(extM3u)
# filenameRe = re.compile('.*?filename=['"](.*?)['"]')
# filename = regParse(filenameRe, body.decode('utf8'))
# file = File(fileTemp, name=filename)
# m3u = M3u(titleField=filename, fileField=file)
# m3u.save()

def get_single_pdf(file_obj, context):
    template_name = get_tex_template_name(file_obj)
    return compile_template_to_pdf(template_name, context)


def download_all_rows_view(request, pk):
    texfile_pk = int(request.POST.get("texfileselected_pk"))
    texfile_obj = TexFile.objects.get(pk=texfile_pk)
    template_name = get_tex_template_name(texfile_obj)

    context = {'text': 'Bar'}
    pdf = get_single_pdf(texfile_obj, context)
    print(type(pdf))
    return render_to_pdf(request, template_name, context, filename='test.pdf')


def download_a_certain_row_view(request, pk, pk_row):
    pass
