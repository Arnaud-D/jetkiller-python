import matplotlib.pyplot as plt
import numpy as np


def export_figure(colormap):
    x = np.linspace(-np.pi, np.pi, 100)
    y = np.linspace(-np.pi, np.pi, 100)
    xv, yv = np.meshgrid(x, y)
    z = np.sin(xv) * np.sin(yv)
    plt.contourf(x, y, z, 200)
    plt.set_cmap(colormap)
    plt.savefig('test_image_' + colormap + '.png')


def main():
    export_figure("jet")
    export_figure("viridis")


if __name__ == "__main__":
    main()
