from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.htmx_form, name='form'),

]
