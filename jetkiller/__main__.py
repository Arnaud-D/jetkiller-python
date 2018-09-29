import sys
import argparse
import jetkiller.file as jkfi
import jetkiller.config as cfg


def parse_args(argv):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?", default=None)
    parser.add_argument("-cm", "--colormap", type=str, default=cfg.default_output_colormap)
    args = parser.parse_args(argv)
    return args


def main(argv=None):
    """Main entry-point."""
    args = parse_args(argv)

    try:
        jkfi.convert_file(args.input_file, args.output_file, args.colormap)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


if __name__ == "__main__":
    main()
