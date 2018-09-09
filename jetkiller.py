from PIL import Image
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import sys


def read_image(input_filename):
    im = Image.open(input_filename, mode="r")
    im_converted = im.convert(mode="RGBA")
    return im_converted


def write_image(output_filename, im):
    im.save(output_filename)


def viridis_map():
    cmap = np.round(np.array(cm.get_cmap("viridis").colors) * 256)
    return np.array([(list(m) + [255]) for m in cmap], dtype=float)


def jet_map():
    n = 256
    r = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['red']) * n
    g = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['green']) * n
    b = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['blue']) * n
    data = np.zeros_like(viridis_map(), dtype=int)
    for i in range(len(r)):
        data[i, 0] = int(round(r[i]))
        data[i, 1] = int(round(g[i]))
        data[i, 2] = int(round(b[i]))
    return np.array([[d[0], d[1], d[2], 255] for d in data], dtype=float)


def is_grey(r, g, b):
    return r == g and r == b


def convert_image(im):
    data = np.asarray(im)
    data_float = data.astype(float)
    data_out = np.zeros_like(data_float)
    j_map = jet_map()
    v_map = viridis_map()
    for i in range(len(data)):
        for j in range(len(data[i])):
            r = data_float[i, j, 0]
            g = data_float[i, j, 1]
            b = data_float[i, j, 2]
            if is_grey(r, g, b):
                data_out[i, j] = np.array([r, g, b, 255])
            else:
                d = (j_map[:, 0] - r) ** 2 + (j_map[:, 1] - g) ** 2 + (j_map[:, 2] - b) ** 2
                idx_min = np.argmin(d)
                data_out[i, j] = v_map[idx_min]
    im2 = Image.fromarray(data_out.astype(data.dtype), mode="RGBA")
    return im2


def jetkiller(input_filename, output_filename):
    # Read input image
    try:
        input_image_data = read_image(input_filename)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)

    # Convert image to new colormap
    output_image_data = convert_image(input_image_data)

    # Write output image
    try:
        write_image(output_filename, output_image_data)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


def main():
    jetkiller("tests/test_input_1.png", "tests/test_result_viridis_.png")


if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
