#
# # Create your views here.
# from django.http import Http404
# from django.http import HttpResponse
# from .models import Album
# # from django.template import loader
# from django.shortcuts import render, get_object_or_404
#
# def index(request):
#
#     all_albums = Album.objects.all()
#     # template = loader.get_template('music/index.html')
#
#     return render(request, 'music/index.html', {'all_albums': all_albums})
#
#
# def index1(request):
#     return HttpResponse("<h1>This is index1</h1>")
#
#
# def detail(request, album_id):
#     #album = Album.objects.get(pk =album_id)
#     album = get_object_or_404(Album, pk=album_id)
#
#     return render(request, 'music/details.html', {'album': album})

from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'
















