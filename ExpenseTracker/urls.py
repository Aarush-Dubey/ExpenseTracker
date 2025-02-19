from django.contrib import admin
from django.urls import path, include
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  
    path('admin/', admin.site.urls),
    path('expense/', include('expense.urls')),
    path('saving/', include('savings.urls')),
    path('user/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
