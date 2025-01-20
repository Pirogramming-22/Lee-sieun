from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('new/', views.post_new, name= 'post_new'),
    path('like/', views.like_ajax, name='like_ajax'),

    path('comment/add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
