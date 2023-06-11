from django.urls import path
from userapp.views import submit_form

urlpatterns = [
    path('submit/', submit_form, name='submit_form'),
]