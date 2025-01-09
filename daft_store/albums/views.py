from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from django.contrib.auth.decorators import login_required
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id) 
    return render(request, 'albums/album_detail.html', {'album': album})

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list') 
    else:
        form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})

