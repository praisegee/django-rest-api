from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register('task', views.TaskListDetailAPI, basename='task')


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.TaskListDetailAPI.as_view()),
    path('<int:pk>/', views.TaskListDetailAPI.as_view()),
    path('<int:id>/update/', views.update_task),
    path('<int:id>/delete/', views.delete_task),
    path('create/', views.TaskListDetailAPI.as_view()),
]
