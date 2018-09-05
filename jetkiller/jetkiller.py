
def read_image(input_filename):
    pass


def write_image(output_filename, img_data):
    pass


def convert_pixel(r, g, b):
    pass


def convert_image(img_data):
    pass


def jetkiller(input_filename, output_filename):
    input_image_data = read_image(input_filename)
    output_image_data = convert_image(input_image_data)
    write_image(output_filename, output_image_data)

