from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verification/', include('verify_email.urls')),
    path('', include('src.base_user.urls')),
    path('', include('src.seeker.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
    # path('verification/', include('verify_email')),

]
