from django import forms
from django.shortcuts import render, redirect, get_object_or_404

from myMusipApp.album.models import Album
from myMusipApp.profiles.models import Profile


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner', ]
        widgets = {
            'album_name': forms.TextInput(attrs=
                                          {'placeholder': 'Album Name'}),
            'artist_name': forms.TextInput(attrs=
                                           {'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs=
                                           {'placeholder': 'Description'}),
            'image_url': forms.TextInput(attrs=
                                         {'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs=
                                       {'placeholder': 'Price'}),
        }


def add_album_page(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST or None)
        if form.is_valid():
            form.instance.owner_id = Profile.objects.first().id
            form.save()
            return redirect('index')

    else:
        form = CreateAlbumForm()

    context = {'form': form}
    return render(request, 'albums/album-add.html', context)


def album_details(request, pk: int):
    album = get_object_or_404(Album, pk=pk)
    context = {'album': album}
    return render(request, 'albums/album-details.html', context)


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']


def album_edit(request, pk: int):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'albums/album-edit.html', context)


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        widgets = {
            'album_name': forms.TextInput(attrs=
                                          {'disabled': 'disabled',
                                           'readonly': 'readonly'}),
            'artist_name': forms.TextInput(attrs=
                                           {'disabled': 'disabled',
                                            'readonly': 'readonly'}),
            'description': forms.TextInput(attrs=
                                           {'disabled': 'disabled',
                                            'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs=
                                         {'disabled': 'disabled',
                                          'readonly': 'readonly'}),
            'price': forms.NumberInput(attrs=
                                       {'disabled': 'disabled',
                                        'readonly': 'readonly'}),
        }

def album_delete(request, pk: int):
    album = Album.objects.get(pk=pk)

    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'albums/album-delete.html', context)
