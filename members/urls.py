from django.urls import path
from . views import UserRegisterView

from .import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),


    path("password_reset/",
         views.password_reset_request, name="password_reset"),


]
