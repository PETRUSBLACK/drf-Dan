from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import (WatchListAV, WatchDetailAV, StreamPlatformVS,
                    StreamPlatformAV, StreamPlatformDetailAV, 
                    ReviewList, ReviewDetail, ReviewCreate, UserReview)

router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # path('list', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-detail')
    path('', include(router.urls)),
    path('list', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream'),
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path("<int:pk>/review-create", ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-Detail'),
    # path('reviews/<str:username>', UserReview.as_view(), name='user-review-Detail'),
    path('reviews/', UserReview.as_view(), name='user-review-Detail'),
]