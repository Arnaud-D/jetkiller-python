import numpy as np
import pytest
import jetkiller.image as jkim
from PIL import Image


@pytest.fixture
def data_array():
    return np.array([[[128, 128, 128], [4, 5, 6]],
                     [[128, 128, 128], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]],
                     [[254, 254, 255], [255, 255, 255]]])


@pytest.fixture
def image():
    return Image.new("RGB", (10, 11))


def test_convert_image_1(image):
    assert isinstance(jkim.convert_image(image), Image.Image)


def test_convert_image_2(image):
    assert image.size == jkim.convert_image(image).size


def test_array2image_1(data_array):
    assert isinstance(jkim.array2image(data_array), Image.Image)


def test_array2image_2(data_array):
    w, h = jkim.array2image(data_array).size
    d1, d2, _ = data_array.shape
    assert w == d2 and h == d1


def test_image2array_1(image):
    assert isinstance(jkim.image2array(image), np.ndarray)


def test_image2array_2(image):
    w, h = image.size
    d1, d2, _ = jkim.image2array(image).shape
    assert w == d2 and h == d1
