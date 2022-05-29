from django.urls import path

from . import views

app_name = 'instance'

urlpatterns = [
    path('', views.instance_page, name='instance'),
    path('add-pattern-instance/', views.add_pattern_instance, name='add-pattern-instance'),
    path('show-pattern-instance-detail/<pattern_instance_id>/', views.show_pattern_instance_detail, name='show-pattern-instance-detail'),
    path('download-pattern-instance/<int:pattern_instance_id>/', views.download_pattern_instance, name='download-pattern-instance'),
]
