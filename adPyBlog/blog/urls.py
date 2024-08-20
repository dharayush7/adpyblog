from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("add/", views.handleAddBlog, name="addBlog"),
    path('test/', views.test),
    path("<slug:slug>", views.post, name="post" ),
    path("comment/", views.handleComment, name="handelcoment"),
    
]