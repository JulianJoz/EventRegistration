# registration_app/urls.py

from django.urls import path
from .views import registration_form, confirmation_page

urlpatterns = [
    path('registration/', registration_form, name='registration_form'),
    path('confirmation/<int:registration_id>/', confirmation_page, name='confirmation'),
]
