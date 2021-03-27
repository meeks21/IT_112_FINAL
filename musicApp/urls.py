from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist, name='artist'),
    path('review/', views.review, name='review'),
    path('songDetail/<int:id>', views.songDetail, name='detail'),
    path('reviewDetail/<int:id>', views.reviewDetail, name='reviewdetail'),
    path('newartist/', views.newArtist, name='newartist'),
    path('newsong/', views.newSong, name='newsong'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('loginmessage/', views.logoutmessage, name='logoutmessage'),
]