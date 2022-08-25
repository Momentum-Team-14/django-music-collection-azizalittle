from django.shortcuts import render, get_object_or_404
from . models import Album
from albums.forms import AlbumForm
from django.shortcuts import redirect
# from django.views.generic import UpdateView

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST) 
        if form.is_valid():
            album = form.save()
            return redirect('list_albums')
    form = AlbumForm()
    return render(request, 'albums/create_albums.html', {'form':form})

# when the link is clicked, it will follow the path to confirm_delete. if user selects ye, then album_list = album_list.remove(album (something to do with pk?))
def confirm_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
    return redirect('list-albums')

# how do i call the form on anexisting album from it's detail page?
def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/edit_album.html', {'album': album})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})
