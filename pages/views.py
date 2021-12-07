from django.shortcuts import render

# Create your views here.


def landing_page_view(request):
    context = {}
    return render(request, 'landing_page.html', context)

def privacy_policy_view(request):
    context = {}
    return render(request, 'privacy_policy.html', context)

def terms_of_service_view(request):
    context = {}
    return render(request, 'terms_of_service.html', context)
