from django.urls import path

from . import views

app_name = 'pattern'

urlpatterns = [
    path('', views.pattern_page, name='pattern'),
]
