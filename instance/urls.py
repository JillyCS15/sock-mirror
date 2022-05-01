from django.urls import path

from . import views

app_name = 'instance'

urlpatterns = [
    path('', views.instance_page, name='instance'),
]
