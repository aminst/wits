import sys
import pandas as pd

def main():
    """
    sample usage: python diplomatic_exchange_modifier.py <initial_dip_exchange_path> <country_names_path> <nodelist_path> <output_path>
    """
    initial_dip_exchange_path = sys.argv[1]
    country_names_path = sys.argv[2]
    nodelist_path = sys.argv[3]
    output_path = sys.argv[4]

    de = pd.read_csv(initial_dip_exchange_path)
    country_names = pd.read_csv(country_names_path, sep=':')
    nl = pd.read_csv(nodelist_path)

    for idx, row in country_names.iterrows():
        de.loc[de["Destination"] == row["country_name"], "Destination"] = row["country_iso3"]
        de.loc[de["Country"] == row["country_name"], "Country"] = row["country_iso3"]    

    for cnt in set(de["Country"].unique()).union(set(de["Destination"].unique())) - set(nl["country_iso3"].unique()):
        de.drop(de[de["Country"] == cnt].index, inplace=True)
        de.drop(de[de["Destination"] == cnt].index, inplace=True)

    de = de.rename(columns={"Destination": "target", "Country": "source"})
    de.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()
