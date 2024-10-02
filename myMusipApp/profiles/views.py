from django.shortcuts import render


def profile_details(request):
    context = {}
    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    context = {}
    return render(request, 'profiles/profile-delete.html', context)
