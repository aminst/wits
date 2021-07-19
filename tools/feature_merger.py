import sys
import pandas as pd

def main():
    """
    sample usage: feature_merger.py <input1_path> <input2_path> <merged_path>
    """
    input1_path = sys.argv[1]
    input2_path = sys.argv[2]
    merged_path = sys.argv[3]

    input1_df = pd.read_csv(input1_path)
    input2_df = pd.read_csv(input2_path)

    merged = pd.merge(input1_df, input2_df, how="left", on=["country_iso3"])
    merged.to_csv(merged_path, index=False)

if __name__ == '__main__':
    main()
