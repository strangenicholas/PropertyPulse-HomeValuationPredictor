from django.urls import path
from . import views


urlpatterns = [
        path('', views.login_view, name='login'),
    # path('', views.predict_price, name='default'), 
    path('accounts/profile/', views.predict_price, name='profile'),  # Replace YourProfileView with your actual view
    
]