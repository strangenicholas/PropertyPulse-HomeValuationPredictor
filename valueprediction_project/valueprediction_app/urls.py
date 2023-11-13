from django.urls import path
from . import views

# urlpatterns = [
#     path('predict/', views.predict_price, name='predict_price'),
# ]

urlpatterns = [
    path('', views.predict_price, name='default'),  # Define a view for the empty string path
    path('predict/', views.predict_price, name='predict_price'),
    # Add more URL patterns specific to your app's views
]