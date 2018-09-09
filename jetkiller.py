from PIL import Image
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import sys
import argparse


# Parameters of internal image representation
internal_mode = "RGBA"
internal_type = float


def read_image(input_filename):
    im = Image.open(input_filename, mode="r")
    im_converted = im.convert(mode=internal_mode)
    return im_converted


def write_image(output_filename, im):
    im.save(output_filename)


def viridis_map():
    cmap = np.round(np.array(cm.get_cmap("viridis").colors) * 256)
    return np.array([(list(m) + [255]) for m in cmap], dtype=internal_type)


def jet_map():
    n = 256
    r = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['red']) * n
    g = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['green']) * n
    b = mpl.colors.makeMappingArray(256, cm.jet._segmentdata['blue']) * n
    data = np.zeros_like(viridis_map())
    for i in range(len(r)):
        data[i, 0] = round(r[i])
        data[i, 1] = round(g[i])
        data[i, 2] = round(b[i])
    return np.array([[d[0], d[1], d[2], 255] for d in data], dtype=internal_type)


def convert_image(im, input_cmap, output_cmap):
    input_data = np.asarray(im)
    output_data = np.zeros_like(input_data)
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            r = input_data[i, j, 0]
            g = input_data[i, j, 1]
            b = input_data[i, j, 2]
            if r == g and g == b:  # Grey pixels
                output_data[i, j, 0] = r
                output_data[i, j, 1] = g
                output_data[i, j, 2] = b
                output_data[i, j, 3] = 255
            else:  # Other pixels
                r_t = (input_cmap[:, 0] - r)
                b_t = (input_cmap[:, 1] - g)
                c_t = (input_cmap[:, 2] - b)
                d = r_t * r_t + b_t * b_t + c_t * c_t
                idx_min = np.argmin(d)
                output_data[i, j] = output_cmap[idx_min]
    output = Image.fromarray(output_data, mode=internal_mode)
    return output


def jetkiller(input_filename, output_filename):
    # Read input image
    input_image_data = read_image(input_filename)
    # Convert image to new colormap
    input_cmap = jet_map()
    output_cmap = viridis_map()
    output_image_data = convert_image(input_image_data, input_cmap, output_cmap)
    # Write output image
    write_image(output_filename, output_image_data)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    try:
        jetkiller(args.input_file, args.output_file)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


if __name__ == "__main__":
    main()
