from django.urls import path, include

from myMusipApp.album.views import add_album_page, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', add_album_page, name='add-album-page'),
    path('<int:pk>/', include([
        path('details/', album_details, name='album-details'),
        path('edit/', album_edit, name='album-edit'),
        path('delete/', album_delete, name='album-delete'),
    ])),
]
