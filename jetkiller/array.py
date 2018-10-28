import numpy as np
from matplotlib import cm
import functools
import jetkiller.config as cfg

# Internal package parameters
_colormap_size = 512
_nint = 255
_type = float
_cache_size = 1024


def get_colormap(colormap):
    """Return a colormap as an array. `colormap` is any name recognized by matplotlib."""
    min_val = 0
    max_val = 1
    cmap = cm.get_cmap(colormap, _colormap_size)
    data = np.linspace(min_val, max_val, _colormap_size)
    color_table = np.around(cmap(data) * _nint)
    return np.array(color_table[:, 0:len(cfg.mode)], dtype=_type)


def convert_array(data, colormap=cfg.default_output_colormap):
    """Convert an image array from the "jet" colormap to a better one."""

    input_cmap = get_colormap(cfg.default_input_colormap)
    output_cmap = get_colormap(colormap)

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
                data[i, j, 0:3] = convert_pixel(r, g, b)
    return data
