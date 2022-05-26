from django.urls import path

from . import views

app_name = 'pattern'

urlpatterns = [
    path('', views.pattern_page, name='pattern'),
    path('delete_shacl_pattern/<shacl_pattern_id>', views.delete_shacl_pattern, name='delete-shacl-pattern'),
]
