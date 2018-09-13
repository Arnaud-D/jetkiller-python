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

To install Jet Killer, use the following command :

```
pip install jetkiller
```

It will make the `jetkiller` command described below available.

## Usage

Jet Killer is designed to be used from the command line.

The following command converts `input_file` to `output_file`:

```
jetkiller input_file output_file
```

If you omit the `output_file`, Jet Killer converts `input_file` to
the default output file "output.png":

```
jetkiller input_file
```

If "output.png" already exists, it is overwritten without any warning.


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
