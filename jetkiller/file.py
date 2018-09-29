from PIL import Image
import jetkiller.image as jkim
import jetkiller.config as cfg
from pathlib import Path


def convert_file(input_filename, output_filename=None, colormap=cfg.default_output_colormap):
    """Convert an image file from the "jet" colormap to a better one."""
    input_image_data = read_image(input_filename)
    output_image_data = jkim.convert_image(input_image_data, colormap)
    if output_filename is None:
        input_path = Path(input_filename)
        output_basename = input_path.stem + cfg.default_output_suffix + input_path.suffix
        output_filename = str(input_path.parent / output_basename)
    write_image(output_filename, output_image_data)


def read_image(input_filename):
    """Read an image from a file."""
    image = Image.open(input_filename)
    image_converted = image.convert(mode=cfg.mode)
    return image_converted


def write_image(output_filename, image):
    """Save an image to a file."""
    image.save(output_filename)
