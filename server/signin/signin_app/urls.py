from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='reg_app'),
]
