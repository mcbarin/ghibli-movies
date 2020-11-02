from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .utils import get_movies_with_people

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60)

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class GetMovies(APIView):
    def get(self, request, format=None):
        """
        Return a list of movies from Studio Ghibli API.
        """
        movies = get_movies_with_people()
        if movies:
            context = {
                "movies": movies
            }
            return render(request, 'movies.html', context)
        else:
            return HttpResponse("Can't connect to the Studio Ghibli API...")