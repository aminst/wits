import sys
import numpy as np
import pandas as pd

def drop_unused_countries(nodelist_df, all_countries):
    for i, row in nodelist_df.iterrows():
        if row["country_iso3"] not in all_countries:
            nodelist_df.drop(nodelist_df[nodelist_df["country_iso3"] == row["country_iso3"]].index, inplace = True)    

def drop_corresponding_edges(edgelist_df, missing_countries):
    for country in missing_countries:
        edgelist_df.drop(edgelist_df[edgelist_df["source"] == country].index, inplace = True)
        edgelist_df.drop(edgelist_df[edgelist_df["target"] == country].index, inplace = True)

def main():
    """
    sample usage: python missing_handler.py <nodelist_path> <edgelist_path> <out_nodelist_path> <out_edgelist_path>
    """
    nodelist_path = sys.argv[1]
    edgelist_path = sys.argv[2]
    out_nodelist_path = sys.argv[3]
    out_edgelist_path = sys.argv[4]

    edgelist_df = pd.read_csv(edgelist_path)
    all_countries = set.union(set(edgelist_df['source'].unique()), set(edgelist_df['target'].unique()))

    nodelist_df = pd.read_csv(nodelist_path)
    drop_unused_countries(nodelist_df, all_countries)
    nodelist_df = nodelist_df.dropna()

    missing_countries = all_countries - set(nodelist_df["country_iso3"])

    drop_corresponding_edges(edgelist_df, missing_countries)

    nodelist_df.drop_duplicates(inplace = True, subset = ["country_iso3"])
    edgelist_df.drop_duplicates(inplace = True)
    nodelist_df.to_csv(out_nodelist_path, index=False)
    edgelist_df.to_csv(out_edgelist_path, index=False)

if __name__ == '__main__':
    main()
    