from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form-submit', views.formSumit, name="form-submit"),
    path('success', views.success, name="success"),
]
