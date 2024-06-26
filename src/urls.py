from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from src.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)