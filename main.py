import sys
import argparse
import jetkiller as jk


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    try:
        jk.jetkiller(args.input_file, args.output_file)
    except Exception as e:
        # Abort on errors
        print(e, file=sys.stderr)
        exit(type(e).__name__)


if __name__ == "__main__":
    main()