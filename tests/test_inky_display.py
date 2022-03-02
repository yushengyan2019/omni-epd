import unittest
import pytest
import os
import sys
# displayfactory fails to import without this :(
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))) 
from omni_epd import displayfactory
from PIL import Image

image_path = os.path.dirname(os.path.realpath(__file__)) + '/../examples/PIA03519_small.jpg'


class TestInkyDisplay(unittest.TestCase):

    @pytest.mark.skip(reason="requires a connected inky")
    def test_auto_inky_with_color_display(self):
        epd = displayfactory.load_display_driver('inky.impression', {'EPD': {'mode': 'color'}})
        image = Image.open(image_path)
        image = image.resize((epd.width, epd.height))
        epd.display(image)
