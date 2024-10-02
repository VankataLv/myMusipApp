from django import forms
from django.shortcuts import render, redirect

from myMusipApp.album.models import Album
from myMusipApp.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    album_count = Album.objects.filter(owner=profile).count()

    context = {
        'profile': profile,
        'album_count': album_count
    }

    return render(request, 'profiles/profile-details.html', context)


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ()


def profile_delete(request):
    profile = Profile.objects.first()
    
    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-delete.html', context)






