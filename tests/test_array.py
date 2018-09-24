import numpy as np
import jetkiller.array as jkar
import jetkiller.config as cfg
import pytest


@pytest.fixture
def data_array():
    return np.around(np.random.rand(250, 151, 3) * jkar._nint)


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
