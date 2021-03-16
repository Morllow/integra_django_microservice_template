from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_page(request):
    if request.user.is_authenticated:
        return HttpResponse(str(request.user.is_authenticated))
    return redirect('/sign-in')


@login_required
def send_template(request, dir, file):
    path = 'templates/' + dir + '/' + file
    f = open(path, 'rb')
    response = FileResponse(f, content_type='application/force-download')
    return response
