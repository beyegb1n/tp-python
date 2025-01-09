from django.shortcuts import render, get_object_or_404
from .models import Album

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id) 
    return render(request, 'albums/album_detail.html', {'album': album})