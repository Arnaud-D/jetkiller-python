import numpy as np
import jetkiller.array as jkar
import jetkiller.config as cfg
import pytest


@pytest.fixture
def data_array():
    return np.array([[[128, 128, 128], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[254, 254, 255], [255, 255, 255]]])


def test_get_colormap_1():
    assert jkar.get_colormap("viridis").shape == (jkar._colormap_size, len(cfg.mode))


def test_get_colormap_2():
    assert jkar.get_colormap("jet").shape == (jkar._colormap_size, len(cfg.mode))


def test_get_colormap_3():
    assert 0 <= np.max(jkar.get_colormap("viridis")) <= jkar._nint


def test_get_colormap_4():
    assert 0 <= np.max(jkar.get_colormap("jet")) <= jkar._nint


def test_get_colormap_5():
    assert (jkar.get_colormap("viridis") % 1 == 0).all()


def test_get_colormap_6():
    assert (jkar.get_colormap("jet") % 1 == 0).all()


def test_convert_array_1(data_array):
    assert data_array.shape == jkar.convert_array(data_array).shape


def test_convert_array_2(data_array):
    assert (jkar.convert_array(data_array) % 1 == 0).all()


def test_convert_array_3(data_array):
    cmap = jkar.get_colormap("viridis")
    dim1 = range(data_array.shape[0])
    dim2 = range(data_array.shape[1])
    data = jkar.convert_array(data_array, "viridis")
    for i in dim1:
        for j in dim2:
            assert (data[i, j] in cmap) or (data[i, j, 0] == data[i, j, 1] and data[i, j, 1] == data[i, j, 2])
