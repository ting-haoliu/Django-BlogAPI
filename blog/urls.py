from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='blog-home'),  # name => other app route may also have home, so need to clear the name
    path("about/", views.about, name='blog-about'),
]