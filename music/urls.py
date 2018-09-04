from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/raghu/
    path('raghu/', views.index1, name='index1'),

    # /music/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'),

    # /music/<album_id>/favorites
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),

    # /music/<album_id>/unfavorites
    path('<int:album_id>/unfavorite/', views.unfavorite, name='unfavorite')





]