
from django.urls import path , include ,re_path
from rest_framework import routers
from .views import MoviesApiView, PlayApiView ,SearchApiView,WatchApiView ,HomeApiView ,mhome


urlpatterns = [
    path('play/', PlayApiView.as_view()),
    path('search/', SearchApiView.as_view()),
    path('watch/', WatchApiView.as_view()),
    path('home/', HomeApiView.as_view()),
    path('movies/', MoviesApiView.as_view()),
    path('mm/',mhome),
]
