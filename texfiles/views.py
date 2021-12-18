from django_htmx.http import trigger_client_event

from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from utils.sessions import create_or_get_session_object
from django.http import HttpResponse, HttpResponseRedirect
from django.http import FileResponse

from coverletters.models import CoverLetter
from .tasks import process_download
from .models import TexFile

def prepare_the_download_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    if request.method == 'POST':
        result = process_download.delay(request.POST, pk)
        # update number of downloads in the tex file
        texfile_obj = TexFile.objects.get(pk=int(request.POST.get("texfileselected_pk")))
        texfile_obj.downloads = texfile_obj.downloads + 1
        texfile_obj.save()
        context={'task_id': result.task_id, 'object': object}
        return render(request, 'processing_download.html', context)
    return redirect(object.get_update_url()) # we had to add this because if user selects language change in the downloading page, we need to redirect him to somewhere


def download_the_zip_file_view(request, pk):
    session_object, request = create_or_get_session_object(request)
    object = get_object_or_404(CoverLetter, pk=pk, session=session_object)
    response = FileResponse(open(object.zip_file.path, 'rb'))
    trigger_client_event(response, 'ZipFileDownloaded', { },) # I think I dont need this ( not used)
    return response
