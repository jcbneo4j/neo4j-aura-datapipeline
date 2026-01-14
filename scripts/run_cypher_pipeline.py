import argparse
import glob
import os
from neo4j import GraphDatabase

def run_scripts(uri, user, password, cypher_dir, csv_url):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    files = sorted(glob.glob(os.path.join(cypher_dir, "*.cql")))

    with driver.session() as session:
        for path in files:
            with open(path, "r", encoding="utf-8") as f:
                query = f.read()
            print(f"Running {path}...")
            session.run(query, csvUrl=csv_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", required=True)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--cypherdir", required=True)
    parser.add_argument("--csv-url", required=True)
    args = parser.parse_args()

    run_scripts(
        uri=args.uri,
        user=args.user,
        password=args.password,
        cypher_dir=args.cypherdir,
        csv_url=args.csv_url,
    )
