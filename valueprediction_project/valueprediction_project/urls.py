from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('prediction_app/', include('prediction_app.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin site
    path('', include('valueprediction_app.urls')),  # Include app-specific URLs with an empty string
]