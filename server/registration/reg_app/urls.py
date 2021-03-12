from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.signup_view, name='reg_app'),
]
