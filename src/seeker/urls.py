from django.urls import path
from .views import seeker_registration, seeker_info

urlpatterns = [
    path('seek_reg/', seeker_registration),
    path('seek_info/<int:pk>/', seeker_info),
]
