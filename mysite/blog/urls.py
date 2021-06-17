from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='base'),
    path('<slug:slug>/', views.post_detail, name='blog_post_detail'),
]
