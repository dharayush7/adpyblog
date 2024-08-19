from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("<slug:slug>", views.post, name="post" ),
    path("comment/", views.handleComment, name="handelcoment")
]