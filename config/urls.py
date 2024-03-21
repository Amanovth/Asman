from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as docs

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('src.main.urls')),
    path('api/auth/', include('src.accounts.urls')),
    path('api/payment/', include('src.payments.urls')),
    path('api/discount/', include('src.discount.urls')),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += docs
