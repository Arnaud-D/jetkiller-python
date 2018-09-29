import pytest
import jetkiller


def test_convert_file_1():
    """2 args, no colormap."""
    jetkiller.convert_file("tests/test_data/test_input_1.png", "tests/test_data/test_result_1.png")
    assert True


def test_convert_file_2():
    """2 args, no colormap."""
    jetkiller.convert_file("tests/test_data/test_input_2.png", "tests/test_data/test_result_2.png")
    assert True


def test_convert_file_3():
    """1 arg, no colormap."""
    jetkiller.convert_file("tests/test_data/test_input_1.png")
    assert True


def test_convert_file_4():
    """1 arg, wrong colormap."""
    with pytest.raises(Exception) as e:
        jetkiller.convert_file("tests/test_data/test_input_1.png", colormap="blabla")
    assert e.type == ValueError


def test_convert_file_5():
    """1 arg, other colormap."""
    jetkiller.convert_file("tests/test_data/test_input_1.png", colormap="magma")
    assert True


def test_convert_file_6():
    """Protected output."""
    with pytest.raises(Exception) as e:
        jetkiller.convert_file("tests/test_data/test_input_1.png", "tests/test_data/protected_output_file.png")
    assert e.type == PermissionError


def test_convert_file_7():
    """Wrong input type"""
    with pytest.raises(Exception) as e:
        jetkiller.convert_file("tests/test_data/generate_test_images.py", "tests/test_data/protected_output_file.png")
    assert e.type == OSError


def test_convert_file_8():
    """File not found."""
    with pytest.raises(Exception) as e:
        jetkiller.convert_file("tests/test_data/not_existing.png", "tests/test_data/protected_output_file.png")
    assert e.type == FileNotFoundError
