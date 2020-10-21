import argparse
import logging

from imdb.utils import get_imdb_data, process_chart, get_pandas_dataframe

logging.basicConfig(level=logging.INFO)


def run(path, file_format, min_rating, top, extra_info=False):
    data = get_imdb_data("http://www.imdb.com/chart/top")
    movie_list = process_chart(data, top, extra_info)
    df = get_pandas_dataframe(movie_list, extra_info, min_rating)
    if file_format == "csv":
        df.to_csv(path)
    elif file_format == "pdf":
        if extra_info:
            logging.warning(
                "Extra info is only displayed when exporting in CSV format."
            )
        bar = df.plot.barh(
            x="title",
            color=[(0.45, (rating / 10) * 0.8, 0) for rating in df["rating"]],
            figsize=(10, len(df) * 0.5),
        )
        bar.set_xlim([6.0, 10.0])
        for index, value in enumerate(df["rating"]):
            bar.text(value, index, str(value))
        bar.figure.tight_layout()
        bar.figure.savefig(path)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Get top X Movies off of imdb and export information about them."
    )
    arg_parser.add_argument("--path", "-p", required=True, type=str)
    arg_parser.add_argument("--format", "-f", choices=["pdf", "csv"], default="csv")
    arg_parser.add_argument(
        "--min_rating",
        "-m",
        type=float,
        required=False,
        default=0,
    )
    arg_parser.add_argument("--top", "-t", type=int, required=False, default=10)
    arg_parser.add_argument("--extra_info", "-x", action="store_true")
    args = arg_parser.parse_args()
    run(
        path=args.path,
        file_format=args.format,
        min_rating=args.min_rating,
        top=args.top,
        extra_info=args.extra_info,
    )
