# Jet Killer

Jet Killer converts images using the "jet" colormap to the "viridis"
colormap by using directly the pixel values, without any knowledge
about the underlying data.

It can be used as a tool to enhance data visualizations for which
the original dataset is unavailable. Use cases include :

* enhancing figures from sources who made an unfortunate
  colormap choice,
* enhancing graphs for which the original data may be lost,
* enhancing visualizations without having to regenerate it from the
  original dataset.

![Principle](docs/schematic_principle.png)


## Installation

The following command installs the `jetkiller` command
and the `jetkiller` package:

```
pip install jetkiller
```


## Usage

### From the command line

Jet Killer is designed to be used mainly from the command line.

Use the following command to convert `input_file` to `output_file`:

```
jetkiller input_file output_file
```

If you omit the argument `output_file`, Jet Killer converts
`input_file` to "output.png" by default:

```
jetkiller input_file
```

If the file "output.png" already exists, it is overwritten without any
warning.


### From Python

If you wish to use Jet Killer from Python, you can
import the `jetkiller` package and use the `jetkiller` function:

```python
import jetkiller as jk
jk.jetkiller("input_image.png", "output_image.png")
```

The second argument is optional and defaults to "output.png", so that
you can write:

```python
import jetkiller as jk
jk.jetkiller("input_image.png")
```

If the file "output.png" already exists, it is overwritten without any
warning.


## Release History

All releases of this project are listed on the tag page of this
repository.

See [CHANGES.md](CHANGES.md) for more details on the content of each release.


## Versioning

Jet Killer attempts to follow the [Semantic Versioning
Specification](https://semver.org/spec/v2.0.0.html) for its version
numbers.


## License

Jet Killer is distributed under the MIT License. See
[LICENSE-MIT](LICENSE-MIT) for more details.
