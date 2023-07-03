from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/', include('filter.urls')),
    path('create/', include('create.urls')),
    path('update/', include('update.urls')),
    path('delete/', include('delete.urls')),
]

