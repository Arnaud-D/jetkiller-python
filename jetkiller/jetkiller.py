from PIL import Image
import numpy as np
import matplotlib as mpl
from matplotlib import cm


def read_image(input_filename):
    im = Image.open(input_filename)
    return im


def write_image(output_filename, im):
    im.save(output_filename)


def viridis_map():
    cmap = np.round(np.array(cm.viridis.colors) * 256)
    return [(list(m) + [255]) for m in cmap]


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
    return [[d[0], d[1], d[2], 255] for d in data]


def convert_pixel(p, from_map, to_map):
    distances = [(p[0] - e[0]) ** 2 + (p[1] - e[1]) ** 2 + (p[2] - e[2]) ** 2 for e in from_map]
    min_idx = np.argmin(distances)
    return to_map[min_idx]


def convert_image(im):
    data = np.asarray(im)
    data_out = np.zeros_like(data)
    j_map = jet_map()
    v_map = viridis_map()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data_out[i, j] = convert_pixel(data[i, j], j_map, v_map)
    im2 = Image.fromarray(data_out, mode="RGBA")
    return im2


def jetkiller(input_filename, output_filename):
    input_image_data = read_image(input_filename)
    output_image_data = convert_image(input_image_data)
    write_image(output_filename, output_image_data)


if __name__ == "__main__":
    import time
    start = time.time()
    jetkiller("../tests/test_image_jet.png", "../tests/test_result_viridis.png")
    end = time.time()
    print(end - start)
