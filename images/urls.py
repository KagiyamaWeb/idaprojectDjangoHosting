
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.image_upload_view, name='upload'),
    path('detail/<int:image_id>/', views.detail, name='detail'),

]
