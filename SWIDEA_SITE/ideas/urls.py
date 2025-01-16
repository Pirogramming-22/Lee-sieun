from django.urls import path
from ideas import views

app_name = 'ideas'

urlpatterns = [
    path('', views.sort, name='list'),
    path('/create', views.create, name='create'),
    path('/delete/<int:pk>/', views.delete, name='delete'),
    path('/update/<int:pk>/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
]
