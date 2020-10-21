# imdb-parser

## About
imdb-parser is a command-line tool for downloading and displaying top imdb movies
(by user rating) and exporting it either into a graph or as text.

## Get started

Run `pip install -r requirements.pip`.

### Command line arguments
- `path` - Mandatory argument. Output path of pdf or csv
- `format` - pdf/csv. Format in which to export, PDF is a histogram. (default is CSV)
- `min_rating` - Float. Minimum score of the exported movies.
- `top` - Integer. Amount of movies to export. (default is 10)
-

If both `min_rating` and `top` are defined, top X are grabbed from the list of
all movies with a score of at least `min_rating`.

### Examples

`python main.py -p "output.pdf" -f "pdf" -m 2 -t 10`

This command will return a horizontal bar graph of the top 10 movies. Movies with a rating of less than 2 will be cut
off.

`python main.py -p "output.csv" -f "csv" -x`

This command will return a csv of the top 10 movies and provide additional information about the movie's genre,
running time and date of release.

## Testing

## Dev notes
This repository uses black for code formatting (https://github.com/psf/black).
