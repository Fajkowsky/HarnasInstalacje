import argparse

from src import settings, run


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', metavar='url', nargs=1, type=valid_arg)
    return parser


def valid_arg(args):
    for item in settings.sites:
        if item in args:
            return args

    msg = 'Not valid url'
    raise argparse.ArgumentTypeError(msg)


def get_obj(args):
    return {}

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    obj = get_obj(args)

    run(obj, *args.link)