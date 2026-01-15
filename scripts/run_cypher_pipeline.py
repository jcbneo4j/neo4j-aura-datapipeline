import argparse
import glob
import json
import os
from neo4j import GraphDatabase

def run_scripts(uri, user, password, cypher_dir, csv_urls):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    files = sorted(glob.glob(os.path.join(cypher_dir, "*.cql")))
    csv_urls_dict = json.loads(csv_urls)  # Parse JSON dict

    with driver.session() as session:
        for path in files:
            with open(path, "r", encoding="utf-8") as f:
                query = f.read()
            print(f"Running {path}...")
            session.run(query, csvUrls=csv_urls_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", required=True)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--cypherdir", required=True)
    parser.add_argument("--csv-urls", required=True)  # Now expects JSON dict string
    args = parser.parse_args()

    run_scripts(
        uri=args.uri,
        user=args.user,
        password=args.password,
        cypher_dir=args.cypherdir,
        csv_urls=args.csv_urls,
    )
