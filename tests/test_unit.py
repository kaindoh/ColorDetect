"""
Unit tests: testing a small bit of code like function or class in isolation of the system
From the developers perspective
"""
# Whether ()dictionary has the correct image count
# test whether text in the dictionary is what is being written to the image

from ..src.color_detect import ColorDetect
import os
import pytest


def test_image_parsed_to_class(image):
    """
    test whether an image is parsed to the class ColorDetect(<image>)
    """
    # import pdb; pdb.set_trace()
    # ColorDetect(image)
    pass


def test_foo(datadir):
    expected_image = datadir.join('image2.jpg')
    ColorDetect(expected_image)
   

def test_dictionary_has_correct_image_count():
    pass

def test_what_is_in_dictionary_is_being_written():
    """
    What is in the dictionary should be what is being written
    """