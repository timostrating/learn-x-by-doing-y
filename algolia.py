import os
import csv

from algoliasearch.search_client import SearchClient


client = SearchClient.create("08KMSERF1B", os.environ["ACTIONS_KEY"])
index = client.init_index("Project")


def add_records(filename: str):

    with open(filename, newline="") as f:
        csv_r = list(csv.DictReader(f, delimiter=";"))
        len_idx = index.search("")["nbHits"]

        if len(csv_r) > len_idx:
            index.save_objects(
                csv_r[len_idx:], {"autoGenerateObjectIDIfNotExist": "true"}
            )
            print(f"{len(csv_r[len_idx:]) - 1} new records added.")
            return

    print("Nothing new.")


if __name__ == "__main__":
    add_records("/github/workspace/projects.csv")