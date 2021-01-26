from django.conf.urls import include
from django.urls import re_path

from rest_framework import routers

from color_swatch import views

router = routers.DefaultRouter()

#Application Views
router.register('color_palette', views.ColorViewSet)

urlpatterns = (
    re_path(r'^v1/', include(router.urls)),
)