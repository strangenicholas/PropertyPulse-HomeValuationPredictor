from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_price, name='predict_price'),
]