from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import MoviesViewSet, CommentsViewSet, TopMoviesView

router = DefaultRouter()
router.register(r'movies', MoviesViewSet)
router.register(r'comments',CommentsViewSet)

urlpatterns=[
     path('', include(router.urls)),
     path('top/',TopMoviesView.as_view())
]
