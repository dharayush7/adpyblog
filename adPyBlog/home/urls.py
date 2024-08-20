from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('login/', views.handelLogin, name="login"),
    path('signup/', views.signup, name="signup"),
    path("logout/", views.handelLogout, name="logout"),
    path('about/', views.about, name="contact"),
    path('user/<str:username>', views.profile, name="profile")
]