from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('<int:id>/', views.get_task),
    path('<int:id>/update/', views.update_task),
    path('<int:id>/delete/', views.delete_task),
    path('create/', views.create_task),
]
