import sys
import argparse
import jetkiller.file as jkfi
import jetkiller.config as cfg
import jetkiller.gui as gui


def parse_args(argv):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action='store_true')
    parser.add_argument("input_file", nargs="?", default=None)
    parser.add_argument("output_file", nargs="?", default=None)
    parser.add_argument("-cm", "--colormap", type=str, default=cfg.default_output_colormap)
    args = parser.parse_args(argv)
    return args


def main_cl(args):
    """Entry-point of the command-line interface"""
    try:
        jkfi.convert_file(args.input_file, args.output_file, args.colormap)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


def main_gui():
    """Entry-point of the graphical user interface."""
    gui.main()


def main(argv=None):
    """Main entry-point."""
    args = parse_args(argv)
    if args.gui:
        main_gui()
    else:
        main_cl(args)


if __name__ == "__main__":
    main()
