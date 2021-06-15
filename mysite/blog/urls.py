from . import views
from django.urls import path

urlpatterns = [
    path('blogs/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='blog_post_detail'),
]
