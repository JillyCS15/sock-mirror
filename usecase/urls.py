from django.urls import path

from . import views

app_name = 'usecase'

urlpatterns = [
    path('', views.usecase_page, name='usecase'),
]
