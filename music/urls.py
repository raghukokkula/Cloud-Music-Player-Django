from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/raghu/
    path('raghu/', views.index1, name='index1'),

    # /music/712/
    path('<int:album_id>/', views.detail, name='detail')


]