import argparse

from imdb.utils import get_imdb_data


def run(path, format, min_score, top, extra_info=False):
    data = get_imdb_data("http://www.imdb.com/chart/top")


if __name__ == '__main__':
    # possible arguments: min score, top X movies,
    # max top is 250
    arg_parser = argparse.ArgumentParser(
        description="Get top X Movies off of imdb and export information about them."
    )
    arg_parser.add_argument(
        "--path",
        "-p",
        required=True,
        help="",
        type=str
    )
    arg_parser.add_argument(
        "--format",
        "-f",
        choices=["pdf", "csv"],
        default="csv",
        help=""
    )
    arg_parser.add_argument(
        "--min_score",
        "-m",
        type=float,
        required=False,
        default=0,
        help="",
    )
    arg_parser.add_argument(
        "--top",
        "-t",
        type=int,
        required=False,
        default=10,
        help=""
    )
    arg_parser.add_argument(
        "--extra_info",
        "-x",
        action="store_true"
    )
    args = arg_parser.parse_args()
    run(
        path=args.p,
        format=args.f,
        min_score=args.m,
        top=args.t,
        extra_info=args.x,
    )
