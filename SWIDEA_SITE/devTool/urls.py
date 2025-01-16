from django.urls import path
from devTool import views

app_name = "devTool"

urlpatterns = [
    path('', views.list, name='list'),
    path('create', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
]
