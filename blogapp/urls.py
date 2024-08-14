# creating list of urls
from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail page



]