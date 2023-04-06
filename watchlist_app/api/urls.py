from django.urls import path, include
# from .views import movie_list, movie_details
from .views import MovieDetailAV, MovieListAV

urlpatterns = [
    # path('list', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-detail')
    path('list', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail')
    
]