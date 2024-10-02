from django import forms
from django.shortcuts import render, redirect

from myMusipApp.album.models import Album
from myMusipApp.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age',]
        widgets = {
            'username': forms.TextInput(attrs=
                                        {'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs=
                                        {'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs=
                                        {'placeholder': 'Age'}),
        }


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}

    return render(request, 'web/home-no-profile.html', context)


def index(request):
    context = {
        'albums': Album.objects.all().order_by('id'),
    }
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return render(request, 'web/home-with-profile.html', context)
