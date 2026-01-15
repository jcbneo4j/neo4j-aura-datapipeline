LOAD CSV WITH HEADERS FROM $csvUrls.rels_csv AS row
MATCH (p:Person {tmdbId: toInteger(row.person_tmdbId)})
MATCH (m:Movie {id: toInteger(row.movieId)})
MERGE (p)-[r:ACTED_IN]->(m)
SET r.role = row.role;

// Set additional node label
//MATCH (p:Person)-[:ACTED_IN]->()
//WITH DISTINCT p
//SET p:Actor;
