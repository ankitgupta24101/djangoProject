from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    dj_text = request.POST.get('text', '')
    dj_email = request.POST.get('email', '')
    params = {'name': dj_text, 'email': dj_email}
    return render(request, 'about.html', params)
    # return HttpResponse("About " + dj_text+' ' + dj_check)
