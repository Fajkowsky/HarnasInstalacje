import argparse
from src import settings

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', metavar='url', nargs=1)
    return parser

def valid_arg(args):
    for item in settings.sites:
        if item in args:
            return True
    return False


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    if valid_arg(*args.link):
        print("Valid url!")
    else:
        print("Not valid url!")

