LOAD CSV WITH HEADERS FROM $csvUrls.movies_csv AS row
MERGE (m:Movie {id: toInteger(row.movieId)})
SET
    m.title = row.title,
    m.imdbId = toInteger(row.movie_imdbId),
    m.languages = split(row.languages, '|'),
    m.genres = split(row.genres, '|');
