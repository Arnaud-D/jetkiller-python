from PIL import Image
import jetkiller.image as jkim
import jetkiller.config as cfg


def convert_file(input_filename, output_filename=cfg.default_output_file, colormap=cfg.default_colormap):
    """Convert an image file from the "jet" colormap to a better one."""
    input_image_data = read_image(input_filename)
    output_image_data = jkim.convert_image(input_image_data, colormap)
    write_image(output_filename, output_image_data)


def read_image(input_filename):
    """Read an image from a file."""
    image = Image.open(input_filename)
    image_converted = image.convert(mode=cfg.mode)
    return image_converted


def write_image(output_filename, image):
    """Save an image to a file."""
    image.save(output_filename)
