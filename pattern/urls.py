from django.urls import path

from . import views

app_name = 'pattern'

urlpatterns = [
    path('', views.pattern_page, name='pattern'),
    path('add_class_pattern/', views.add_class_pattern, name='add-class-pattern'),
    path('add_shacl_pattern/', views.add_shacl_pattern, name='add-shacl-pattern'),
    path('delete_class_pattern/<class_pattern_id>/', views.delete_class_pattern, name='delete-class-pattern'),
    path('delete_shacl_pattern/<shacl_pattern_id>/', views.delete_shacl_pattern, name='delete-shacl-pattern'),
]
