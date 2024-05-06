from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from scr.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('barber.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)