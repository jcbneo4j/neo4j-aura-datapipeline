LOAD CSV WITH HEADERS FROM $csvUrls.persons_csv AS row
MERGE (p:Person {tmdbId: toInteger(row.person_tmdbId)})
SET p.name = row.name, p.born = date(row.born);
