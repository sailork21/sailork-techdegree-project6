from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'minerals'

urlpatterns = [
    #url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    path('', views.mineral_list, name='mineral_list'),
    path('<int:pk>', views.mineral_detail, name='detail'),
    path('random/<int:pk>', views.mineral_random, name='random'),
    ]
