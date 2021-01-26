from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from color_swatch import models


class ColorSerializer(serializers.ModelSerializer):
    color_type = serializers.CharField(read_only=True)

    class Meta:
        model = models.Color
        fields = '__all__'


class RGBColorSerializer(serializers.ModelSerializer):
    hex_color = serializers.CharField(read_only=True)
    color_type = serializers.CharField(read_only=True)

    class Meta:
        model = models.RGBColor
        exclude = ('created', 'modified')


class HSLColorSerializer(serializers.ModelSerializer):
    hex_color = serializers.CharField(read_only=True)
    color_type = serializers.CharField(read_only=True)

    class Meta:
        model = models.HSLColor
        exclude = ('created', 'modified')


class BRGBColorSerializer(serializers.ModelSerializer):
    hex_color = serializers.CharField(read_only=True)
    color_type = serializers.CharField(read_only=True)

    class Meta:
        model = models.BRGBColor
        exclude = ('created', 'modified')


class ColorPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.RGBColor: RGBColorSerializer,
        models.HSLColor: HSLColorSerializer,
        models.BRGBColor: BRGBColorSerializer,
    }
