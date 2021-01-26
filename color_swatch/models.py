import colorsys
import random
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.functional import cached_property
from django.db import models
from polymorphic.models import PolymorphicModel
from django.apps import apps

from django.core.exceptions import ObjectDoesNotExist

class Color(PolymorphicModel, models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @cached_property
    def color_type(self):
        return ''

    def hex_color(self):
        """
        Convert color to hex representation
        """
        msg = "Method hex_color() must be implemented by subclass: `{}`"
        raise NotImplementedError(msg.format(self.__class__.__name__))

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.color_type, self.created)


class RGBColor(Color):
    red = models.SmallIntegerField(
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    green = models.SmallIntegerField(
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    blue = models.SmallIntegerField(
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )

    class Meta:
        unique_together = ('red', 'green', 'blue')

    @cached_property
    def color_type(self):
        return 'rgb'

    @cached_property
    def hex_color(self):
        return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)


class HSLColor(Color):
    hue = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(359)
        ]
    )
    saturation = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(100)
        ]
    )
    lightness = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(100)
        ]
    )

    class Meta:
        unique_together = ('hue', 'saturation', 'lightness')

    @cached_property
    def color_type(self):
        return 'hsl'

    @cached_property
    def hex_color(self):
        r, g, b = colorsys.hls_to_rgb(self.hue / 360, self.lightness / 100, self.saturation / 100)
        return "#{0:02x}{1:02x}{2:02x}".format(round(r * 255), round(g * 255), round(b * 255))


class BRGBColor(Color):
    red = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(10000)
        ]
    )
    green = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(10000)
        ]
    )
    blue = models.SmallIntegerField(
        validators=[
            MaxValueValidator(0),
            MinValueValidator(10000)
        ]
    )

    class Meta:
        unique_together = ('red', 'green', 'blue')

    @cached_property
    def color_type(self):
        return 'brgb'

    @cached_property
    def hex_color(self):
        r, g, b = (self.red / 10000, self.green / 10000, self.blue / 10000)
        return "#{0:02x}{1:02x}{2:02x}".format(round(r * 255), round(g * 255), round(b * 255))
