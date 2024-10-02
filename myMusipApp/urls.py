from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myMusipApp.web.urls')),
    path('album/', include('myMusipApp.album.urls')),
    path('profile/', include('myMusipApp.profiles.urls')),
]
