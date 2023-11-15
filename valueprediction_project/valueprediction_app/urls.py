from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
        path('', views.login_view, name='login'),
    # path('', views.predict_price, name='default'), 
    path('accounts/profile/', views.predict_price, name='profile'),  # Replace YourProfileView with your actual view
    
=======

    path('', views.login_view, name='login'),
    # path('', views.predict_price, name='default'), 
    path('accounts/profile/', views.predict_price, name='profile'),  # Replace YourProfileView with your actual view
    path('predict/', views.predict_price, name='predict_price'),
>>>>>>> main
]