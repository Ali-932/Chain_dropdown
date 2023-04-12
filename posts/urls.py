from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.htmx_form, name='form'),
    path("form/chained_author/", views.htmx_models, name="chained-author"),

]
