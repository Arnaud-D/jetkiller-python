from PIL import Image
import numpy as np
from matplotlib import cm
import functools


# Internal package parameters
_mode = "RGB"
_type = float
_colormap_size = 256
_nint = 255
_cache_size = 1024


def jetkiller(input_filename, output_filename="output.png", colormap="viridis"):
    """Convert an image file from the "jet" colormap to a better one."""
    input_image_data = read_image(input_filename)
    input_cmap = get_colormap("jet")
    output_cmap = get_colormap(colormap)
    output_image_data = convert_image(input_image_data, input_cmap, output_cmap)
    write_image(output_filename, output_image_data)


def read_image(input_filename):
    """Read an image from a file."""
    im = Image.open(input_filename)
    im_converted = im.convert(mode=_mode)
    return im_converted


def get_colormap(colormap):
    """Return a colormap as an array. `colormap` is any name recognized by matplotlib."""
    min_val = 0
    max_val = 1
    cmap = cm.get_cmap(colormap, _colormap_size)
    data = np.linspace(min_val, max_val, _colormap_size)
    color_table = cmap(data) * _nint
    return np.array(color_table[:, 0:3], dtype=_type)


def convert_image(im, input_cmap, output_cmap):
    """Convert an image from a colormap to another."""
    data = np.asarray(im)
    data.setflags(write=True)

    @functools.lru_cache(maxsize=_cache_size)
    def convert_pixel(red, green, blue):
        # Get nearest color from input colormap and return
        # corresponding color in output colormap
        dr = input_cmap[:, 0] - red
        dg = input_cmap[:, 1] - green
        db = input_cmap[:, 2] - blue
        dist = dr * dr + dg * dg + db * db
        idx = np.argmin(dist)
        return output_cmap[idx]

    dim1 = range(data.shape[0])
    dim2 = range(data.shape[1])
    for i in dim1:
        for j in dim2:
            r, g, b = data[i, j, 0], data[i, j, 1], data[i, j, 2]
            if r != g or g != b:  # Grey pixels are not processed
                data[i, j] = convert_pixel(r, g, b)
    return Image.fromarray(data, mode=_mode)


def write_image(output_filename, im):
    """Save an image to a file."""
    im.save(output_filename)
