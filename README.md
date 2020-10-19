# imdb-parser

## About
imdb-parser is a command-line tool for downloading and displaying top imdb movies
(by user rating) and exporting it either into a graph or as text.

## Get started

### Command line arguments
- `path` - Mandatory argument. Output path of pdf or csv
- `format` - pdf/csv. Format in which to export, PDF is a histogram. (default is CSV)
- `minscore` - Float. Minimum score of the exported movies.
- `top` - Integer. Amount of movies to export. (default is 10)

If both `minscore` and `top` are defined, top X are grabbed from the list of
all movies with a score of at least `minscore`.

## Testing

## Dev notes
This repository uses black for code formatting (https://github.com/psf/black).
