from django.urls import path
from. import views

urlpatterns = [
    path('reg/', views.base_user_registration),
    path('base_user/verify_token/', views.base_user_email_verify)
]
