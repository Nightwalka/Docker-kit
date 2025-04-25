from django.contrib import admin
from django.urls import path, include  # <-- include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),   # <-- THIS is the fix
]
