from django.urls import path
from .views import blogListView

Urlpatterns = [ path(' ', blogListView.as_view(), name='home'), 
]