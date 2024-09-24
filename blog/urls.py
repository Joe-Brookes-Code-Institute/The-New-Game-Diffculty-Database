from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('<int:post_id>/edit/', views.edit_blog_post, name='edit_blog_post'),  # Make sure this line is present
]