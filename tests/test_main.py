import pytest
from jetkiller import __main__


def test_main_1():
    """No args."""
    with pytest.raises(SystemExit) as e:
        argv = None
        __main__.main(argv)
    assert e.type == SystemExit


def test_main_2():
    """2 args, no colormap."""
    argv = ["tests/test_data/test_input_1.png", "tests/test_data/test_result_1.png"]
    __main__.main(argv)
    assert True


def test_main_3a():
    """Only one argument"""
    argv = ["tests/test_data/test_input_1.png"]
    __main__.main(argv)
    assert True


def test_main_3b():
    """Only one argument"""
    argv = ["tests/test_data/test_input_2.png"]
    __main__.main(argv)
    assert True


def test_main_4():
    """Wrong argument."""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/test_input_1.png", "--bullshit"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == 2


def test_main_5():
    """Wrong colormap."""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/test_input_1.png", "--colormap", "blabla"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == "ValueError"


def test_main_6():
    """No colormap."""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/test_input_1.png", "--colormap"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == 2


def test_main_7():
    """Other colormap."""
    argv = ["tests/test_data/test_input_1.png", "tests/test_data/test_result_magma.png", "--colormap", "magma"]
    __main__.main(argv)
    assert True


def test_main_8():
    """Protected output."""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/test_input_1.png", "tests/test_data/protected_output_file.png"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == "PermissionError"


def test_main_9():
    """Wrong input type"""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/generate_test_images.py", "tests/test_data/wrong_type.png"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == "OSError"


def test_main_10():
    """File not found."""
    with pytest.raises(SystemExit) as e:
        argv = ["tests/test_data/not_existing.png", "tests/test_data/wrong_type.png"]
        __main__.main(argv)
    assert e.type == SystemExit
    assert e.value.code == "FileNotFoundError"
