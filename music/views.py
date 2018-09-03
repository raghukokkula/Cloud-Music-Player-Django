
# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.shortcuts import render

def index(request):

    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')

    return render(request, 'music/index.html', {'all_albums': all_albums})


def index1(request):
    return HttpResponse("<h1>This is index1</h1>")


def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("This file doesn't exist")

    return render(request, 'music/details.html', {'album': album})

