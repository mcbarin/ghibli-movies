from django.urls import include, path

from core import views

urlpatterns = [
    path('movies/', views.GetMovies.as_view(), name='get_movies'),
]
