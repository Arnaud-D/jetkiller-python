from PIL import Image
import numpy as np
import jetkiller.config as cfg
import jetkiller.array as jkar


def convert_image(image, colormap=cfg.default_output_colormap):
    """Convert an image from the "jet colormap" to a better one."""
    data = image2array(image)
    data = jkar.convert_array(data, colormap)
    output = array2image(data)
    return output


def array2image(array):
    """Convert an array to an image."""
    mode = "RGB" if array.shape[2] == 3 else "RGBA"
    return Image.fromarray(array, mode=mode)


def image2array(image):
    """Convert an image to an array."""
    data = np.asarray(image)
    data.setflags(write=True)
    return data
