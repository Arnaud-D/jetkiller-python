import sys
import argparse
import jetkiller as jk


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?", default="output.png")
    parser.add_argument("-cm", "--colormap", type=str, default="viridis")
    args = parser.parse_args()
    return args


def main():
    """Main entry-point."""
    args = parse_args()

    try:
        jk.jetkiller(args.input_file, args.output_file, args.colormap)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


if __name__ == "__main__":
    main()
