from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("homevaluations/", include("homevaluations.urls")),
    path("admin/", admin.site.urls),
]

