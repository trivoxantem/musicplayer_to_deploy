from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

def song_list_upload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list_upload')
    else:
        form = SongForm()

    songs = Song.objects.all()
    return render(request, 'song_list_upload.html', {'form': form, 'songs': songs})


def song_list_upload(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(title__icontains=query) if query else Song.objects.all()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list_upload')
    else:
        form = SongForm()

    return render(request, 'song_list_upload.html', {'form': form, 'songs': songs, 'query': query})
