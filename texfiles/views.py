from django_htmx.http import trigger_client_event


from django.views.decorators.http import require_POST
from django.shortcuts import render,  get_object_or_404
from utils.sessions import create_or_get_session_object
from django.http import HttpResponse
from django.http import FileResponse

from .tasks import process_download
from coverletters.models import CoverLetter



@require_POST
def prepare_the_download_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    result = process_download.delay(request.POST, pk)
    context={'task_id': result.task_id, 'object': object}
    return render(request, 'processing_download.html', context)


def download_the_zip_file_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    # response = HttpResponse(object.zip_file, content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="{}"'.format('All_coverletters.zip')

    response = FileResponse.set_headers(open(object.zip_file.path, 'rb'))
    trigger_client_event(response, 'ZipFileDownloaded', { },)
    return response





# @require_POST
# def download_all_rows_view(request, pk):
#     go_to_sleep.delay(1)
#     # getting the coverletter object
#     session_object, request = create_or_get_session_object(request)
#     object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
#     coverletter = CoverLetter.objects.get(pk=pk)
#     rows = coverletter.rows.all()
#
#     texfile_pk = int(request.POST.get("texfileselected_pk"))
#     texfile_obj = TexFile.objects.get(pk=texfile_pk)
#     settings.LATEX_INTERPRETER = texfile_obj.interpreter
#     template_name = get_tex_template_name(texfile_obj)
#
#     # getting the data that does not changes
#
#     candidate_name = request.POST.get("candidate_name").strip()
#     candidate_position = request.POST.get("candidate_position").strip()
#     candidate_email = request.POST.get("candidate_email").strip()
#     candidate_phone = request.POST.get("candidate_phone").strip()
#     candidate_location = request.POST.get("candidate_location").strip()
#     candidate_website = request.POST.get("candidate_website").strip()
#     location_date = request.POST.get("location_date").strip()
#
#
#     no_changing_context = {'location_date': location_date, 'candidate_name': candidate_name,
#     'candidate_position': candidate_position, 'candidate_email': candidate_email, 'candidate_phone': candidate_phone, 'candidate_location':candidate_location,'candidate_website': candidate_website}
#
#     filenames =[]
#     files = []
#     for index, row in enumerate(rows):
#         try:
#             filenames.append(f"{index+1}_Application_{row.items.all()[1].name}_{row.items.all()[2].name}/coverletter.pdf")
#         except:
#             filenames.append(f"{index+1}_Application_xxxx_yyyy/coverletter.pdf")
#     for row, filename in zip(rows, filenames):
#         text = request.POST.get("text")
#         company_text = request.POST.get("company_text")
#         applying_position = request.POST.get("applying_position")
#         applying_position = applying_position.strip()
#         for item, column in zip(row.items.all(), coverletter.columns.all()):
#             text = text.replace(column.hashtag.name, item.name)
#             company_text = company_text.replace(column.hashtag.name, item.name)
#             applying_position = applying_position.replace(column.hashtag.name, item.name)
#
#         # text processing
#         text_paragraphs = [line for line in text.splitlines() if line]
#         company_text = '\r\n'.join(line for line in company_text.splitlines() if line)
#         changing_context = {'text_paragraphs': text_paragraphs, 'company_text': company_text, 'applying_position': applying_position}
#         context = {**changing_context, **no_changing_context}
#         pdf = compile_template_to_pdf(template_name, context)
#         files.append((filename, pdf))
#
#
#     full_zip_in_memory = generate_zip(files)
#     response = HttpResponse(full_zip_in_memory, content_type='application/force-download')
#     response['Content-Disposition'] = 'attachment; filename="{}"'.format('All_coverletters.zip')
#
#     return response



















# maybe I will use these ones:


def get_single_pdf(file_obj, context):
    template_name = get_tex_template_name(file_obj)
    return compile_template_to_pdf(template_name, context)



def download_a_certain_row_view(request, pk, pk_row):
    pass
