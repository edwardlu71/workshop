from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='finance_index'),
    path('timeseries', views.timeseries, name='finance_timeseries'),
    path('form', views.form, name='finance_form'),
]
