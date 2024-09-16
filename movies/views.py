from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import movie_data

def detail_movie(request, movie_id):
    context = {'movie': movie_data[movie_id - 1]}
    return render(request, 'movies/detail.html', context)

def list_movies(request):
    context = {"movie_list": movie_data}
    return render(request, 'movies/index.html', context)