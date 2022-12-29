"""
URL mappings for the user API.
"""
from django.urls import path
from user import views


app_name = 'user'  # for `reverse` in URL

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
