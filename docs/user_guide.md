# User Guide

## Installation

### From PyPI

The recommended way to get Jet Killer is to install it from PyPI using
`pip`. If `pip` is not installed on your system, you will have to
install it.

To instal Jet Killer, execute the following command:

```
pip install jetkiller
```

It will install the `jetkiller` command and the `jetkiller` package.

### From the repository

The most flexible way to get Jet Killer is to clone the Git
repository. If `git` is not available on your system, you will have to
install it.

To clone the repository, execute the following command in your
install directory:

```
git clone https://github.com/Arnaud-D/jetkiller.git
```

From there, you can proceed according to your own needs.

## Usage

### Command Line Interface

When installed through `pip`, Jet Killer provide a command line
interface through the `jetkiller` command.

#### Full Syntax

```
jetkiller input_file output_file
```

Convert an image file using the "jet" colormap to
an image file using the "viridis" colormap.

Arguments:

* `input_file`: path to the input file,
* `output_file`: path to the output file.

The input file is read and the image is converted to the "viridis"
colormap. Then, the converted image is written to the output file. If
the output file already exists, it is overwritten without warning.


#### Short Syntax

```
jetkiller input_file
```

Convert an image file using the "jet" colormap to an
image file using the "viridis" colormap.

Arguments:

* `input_file`: path to the input file.

The input file is read and the image is converted to the "viridis"
colormap. Then, the converted image is written to an output file. The
name of the output file is determined from the name of the input file
by suffixing it with "_output" before the extension. For example,
if the input file is "test/image.png", the default output is
"test/image_output.png".

If the output file already exists, it is overwritten without warning.


#### Colormap Selection

```
jetkiller input_file output_file --colormap cmap
```

```
jetkiller input_file output_file -cm cmap
```

```
jetkiller input_file --colormap cmap
```

```
jetkiller input_file -cm cmap
```

Convert an image file using the "jet" colormap to an
image file using the specified colormap.

Arguments:

* `input_file`: path to the input file,
* `output_file`: path to the output file,
* `cmap`: name of the colormap.

For both the full syntax or the short syntax, you can optionnally
specify the output colormap using the `--colormap` argument, or its
short form `-cm`. Any value from the
[matplotlib colormaps](https://matplotlib.org/users/colormaps.html)
is recognized. In the absence of the colormap argument, the colormap
defaults to "viridis".


### Python Package

#### Convert an image file

```
import jetkiller
jetkiller.convert_file(input_file, output_filename=None, colormap="viridis")
```

`convert_file` reads the file whose path is `input_file` and write
it to an output file.

Arguments:

* `input_file`: path to the input file,
* `output_filename`: path to the output file,
* `colormap`: name of the colormap.

The path to the output file is specified using  the argument
`output_filename`. If it is not specified ("None"), then the output
file is determined from the input file by suffixing it with "_output"
before the extension. If the output file already exist, it is
overwritten without warning.

The colormap can be chosen by using the `colormap` argument. The
default value is "viridis". Any colormap from the
[matplotlib colormaps](https://matplotlib.org/users/colormaps.html)
is recognized.

#### Convert a PIL.Image object

```
import jetkiller
image_converted = jetkiller.convert_image(image, colormap="viridis")
```

`convert_image` reads a PIL.Image and converts it to a PIL.Image.

Arguments:

* `image`: PIL.Image object,
* `colormap`: name of the colormap.

This function allows to process an image with Pillow/PIL before
converting them to another colormap. A typical use case is to limit
the conversion to a region instead of the whole image.

The colormap can be chosen by using the `colormap` argument. The
default value is "viridis". Any colormap from the
[matplotlib colormaps](https://matplotlib.org/users/colormaps.html)
is recognized.

#### Convert an array

```
import jetkiller
data_converted = jetkiller.convert_array(data, colormap="viridis")
```

`convert_image` takes an array and converts it in place.

Arguments:

* `data`: h-by-w-by-3 array,
* `colormap`: name of the colormap.

Sometimes, it can be useful to work directly with an array. The array
is 3-dimensional, with each dimension representing respectively
the height of the image, the width image, and the pixel components.

The colormap can be chosen by using the `colormap` argument. The
default value is "viridis". Any colormap from the
[matplotlib colormaps](https://matplotlib.org/users/colormaps.html)
is recognized.
