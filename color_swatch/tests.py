import colorsys
from django.test import TestCase
from color_swatch.models import (
    Color,
    RGBColor,
    HSLColor,
    BRGBColor
)
from django.utils import timezone

# models test
class ColorTest(TestCase):
    def create_color(self, name="random color"):
        return Color.objects.create(name=name)

    def test_color_str(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, Color))
        self.assertEqual(c.__str__(), '{} - {} - {}'.format(c.name, c.color_type, c.created))

    def test_hex_color(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, Color))
        self.assertRaises(NotImplementedError, c.hex_color)


class RGBColorTest(TestCase):
    def create_color(self, name="random rgb color"):
        return RGBColor.objects.create(name=name,red=255,green=255,blue=255)

    def test_color_type(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, RGBColor))
        self.assertEqual(c.color_type, 'rgb')

    def test_hex_color(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, RGBColor))
        self.assertEqual(c.hex_color, "#{0:02x}{1:02x}{2:02x}".format(255, 255, 255))


class HSLColorTest(TestCase):
    def create_color(self, name="random hsl color"):
        return HSLColor.objects.create(name=name,hue=50,saturation=100,lightness=50)

    def test_color_type(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, HSLColor))
        self.assertEqual(c.color_type, 'hsl')

    def test_hex_color(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, HSLColor))
        r, g, b = colorsys.hls_to_rgb(50/360, 50/100, 100/100)
        self.assertEqual(c.hex_color, "#{0:02x}{1:02x}{2:02x}".format(round(r * 255), round(g * 255), round(b * 255)))


class BRGBColorTest(TestCase):
    def create_color(self, name="random brgb color"):
        return BRGBColor.objects.create(name=name,red=1000,green=567,blue=892)

    def test_color_type(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, BRGBColor))
        self.assertEqual(c.color_type, 'brgb')

    def test_hex_color(self):
        c = self.create_color()
        self.assertTrue(isinstance(c, BRGBColor))
        r, g, b = (1000 / 10000, 567 / 10000, 892 / 10000)
        self.assertEqual(c.hex_color, "#{0:02x}{1:02x}{2:02x}".format(round(r * 255), round(g * 255), round(b * 255)))