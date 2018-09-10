from PIL import Image
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import functools


# Parameters of internal image representation
internal_mode = "RGB"
internal_type = float


def read_image(input_filename):
    im = Image.open(input_filename)
    im_converted = im.convert(mode=internal_mode)
    return im_converted


def write_image(output_filename, im):
    im.save(output_filename)


def viridis_map():
    cmap = np.round(np.array(cm.get_cmap("viridis").colors) * 256)
    return np.array(cmap, dtype=internal_type)


def jet_map():
    n = 256
    r = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['red']) * n
    g = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['green']) * n
    b = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['blue']) * n
    data = np.zeros_like(viridis_map())
    for i in range(len(r)):
        data[i, 0] = r[i]
        data[i, 1] = g[i]
        data[i, 2] = b[i]
    return np.array(np.around(data), dtype=internal_type)


def convert_image(im, input_cmap, output_cmap):
    data = np.asarray(im)
    data.setflags(write=True)

    @functools.lru_cache(maxsize=1024)
    def convert_pixel(red, green, blue):
        dr = input_cmap[:, 0] - red
        dg = input_cmap[:, 1] - green
        db = input_cmap[:, 2] - blue
        dist = dr * dr + dg * dg + db * db
        idx = np.argmin(dist)
        return output_cmap[idx]

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            r, g, b = data[i, j, 0], data[i, j, 1], data[i, j, 2]
            if r != g or g != b:  # We do nothing for grey pixels
                data[i, j] = convert_pixel(r, g, b)
    return Image.fromarray(data, mode=internal_mode)


def jetkiller(input_filename, output_filename):
    # Read input image
    input_image_data = read_image(input_filename)
    # Convert image to new colormap
    input_cmap = jet_map()
    output_cmap = viridis_map()
    output_image_data = convert_image(input_image_data, input_cmap, output_cmap)
    # Write output image
    write_image(output_filename, output_image_data)
