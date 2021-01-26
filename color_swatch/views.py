from rest_framework import viewsets

from color_swatch import models
from color_swatch import serializers

SWATCH_COLOR_LIMIT = 5


class ColorViewSet(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorPolymorphicSerializer

    def get_queryset(self):
        return models.Color.objects.order_by('?')[:SWATCH_COLOR_LIMIT]
