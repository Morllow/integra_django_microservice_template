from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='reg_app'),
    path('logout/', views.logout_view, name='logout_view')
]
