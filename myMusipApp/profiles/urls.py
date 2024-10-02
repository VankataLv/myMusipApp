from django.urls import path

from myMusipApp.profiles.views import profile_details, profile_delete

urlpatterns = [
    path('details/', profile_details, name='profile-details'),
    path('delete/', profile_delete, name='profile-delete'),
]