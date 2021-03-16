from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/<str:dir>/<str:file>', views.send_template, name='send template view'),
    path('', views.index_page, name='index_page'),
]
