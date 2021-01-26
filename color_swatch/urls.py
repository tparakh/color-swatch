from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

api_patterns = [
    path('color_swatch/', include('color_swatch.apiurls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
