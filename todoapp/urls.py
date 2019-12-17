from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('home/', views.home, name='home'),
path('update/<str:pk>/', views.updatetask, name='updatetask'),
path('delete/<str:pk>/', views.deletetask, name='deletetask'),
]
