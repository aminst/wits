import sys
import numpy as np
import pandas as pd

def main():
    """
    sample usage: python colony_modifier.py <nodelist_path> <colonies_base_path> <output_path>
    """
    nodelist_path = sys.argv[1]
    colonies_base_path = sys.argv[2]
    output_path = sys.argv[3]

    countries = pd.read_csv(nodelist_path)
    colonies = pd.read_csv(colonies_base_path)

    adj_matrix = np.zeros((len(countries), len(countries)))
    country2idx = {}
    for idx, row in countries.iterrows():
        country2idx[row["country_iso3"]] = idx

    for idx, row in colonies.iterrows():
        if (row["country_iso3"] not in country2idx) or (row["colonizer"] not in country2idx):
            continue
        adj_matrix[country2idx[row["country_iso3"]], country2idx[row["colonizer"]]] = 1

    adj_df = pd.DataFrame(data = adj_matrix, index = country2idx.keys(), columns = country2idx.keys())
    edgelist = adj_df.stack().reset_index()
    edgelist = edgelist.rename(mapper={"level_0": "source", "level_1": "target", 0: "colonization"}, axis=1)
    edgelist.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()
