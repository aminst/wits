import sys
import numpy as np
import pandas as pd

def create_aggregate_df(trades, index_to_country):
    df = pd.DataFrame()
    for i in range(trades.shape[0]):
        for j in range(trades.shape[0]):
            if trades[i, j] != 0:
                df = df.append({
                    'source': index_to_country[i], 
                    'target': index_to_country[j], 
                    'weight': trades[i, j]
                }, ignore_index=True)
    return df

def aggregate_trades(dataframe, country_to_index, all_countries):
    trades = np.zeros((len(all_countries), len(all_countries)))
    for index, row in dataframe.iterrows():
        trades[
            country_to_index[row['ReporterISO3']], 
            country_to_index[row['PartnerISO3']]
        ] += row['TradeValue']
    return trades

def get_country_index_dicts(dataframe):
    all_countries = set.union(set(dataframe['PartnerISO3'].unique()), set(dataframe['ReporterISO3'].unique()))
    country_to_index = {}
    for index, country in enumerate(all_countries):
        country_to_index[country] = index
    index_to_country = {val: key for key, val in country_to_index.items()}  

    return country_to_index, index_to_country, all_countries

def main():
    """
    sample usage: python trade_cleaner.py <uncleaned_file_path> <cleaned_file_output_path>
    """
    if len(sys.argv) != 3:
        print("Please provide data path and output file name!")
        exit()

    file_path = sys.argv[1]
    output_name = sys.argv[2]

    df = pd.read_csv(file_path)
    df.drop(['NetWeight', 'Year', 'QuantityToken', 'ProductCode', 'TradeFlow', 'DestNomenCode', 'SourceNomenCode', 'Quantity'], axis=1, inplace=True)
    country_to_index, index_to_country, all_countries = get_country_index_dicts(df)
    trades = aggregate_trades(df, country_to_index, all_countries)
    agg_df = create_aggregate_df(trades, index_to_country)
    agg_df.to_csv(output_name, index=False)


if __name__ == '__main__':
    main()
    