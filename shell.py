import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="None", help='path')
    args = parser.parse_args()
    sys.stdout.write(str(path_print(args)))


def path_print(args):
    return args.path


if __name__ == "__main__":
    main()
