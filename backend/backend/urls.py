from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Add accounts routes
    path('', include('home.urls')),  # Assuming you have a home app
]
