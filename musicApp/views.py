from django.shortcuts import render, get_object_or_404
from .models import Artist, SongName, Review
from django.urls import reverse_lazy
from .forms import ArtistForm, SongForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'musicApp/index.html')

def artist(request):
    artist_list=Artist.objects.all()
    return render(request, 'musicApp/artist.html', {'artist_list': artist_list})

def review(request):
    review=Review.objects.all()
    return render(request, 'musicApp/review.html', {'review': review})

def songDetail(request, id):
    song=get_object_or_404(SongName, pk=id)
    return render(request, 'musicApp/songdetail.html', {'song' : song})

def reviewDetail(request, id):
    review=get_object_or_404(Review, pk=id)
    return render(request, 'musicApp/reviewdetail.html', {'review' : review})

@login_required
def newArtist(request):
    form=ArtistForm

    if request.method=='POST':
        form=ArtistForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ArtistForm()
    else:
        form=ArtistForm()
    return render(request, 'musicApp/newartist.html', {'form': form})

@login_required
def newSong(request):
    form=SongForm

    if request.method=='POST':
        form=SongForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=SongForm()
    else:
        form=SongForm()
    return render(request, 'musicApp/newsong.html', {'form': form})

@login_required
def newReview(request):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'musicApp/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'musicApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'musicApp/logoutmessage.html')