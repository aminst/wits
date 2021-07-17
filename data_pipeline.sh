python tools/trade_cleaner.py data/Trade_BEH0_2011_Export_2020Jul10.csv tmp/trades.csv
python tools/feature_merger.py data/features/gdp_2011.csv data/features/inflation_2011.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/gdp_growth_2011.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/colonization.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/geo_cepii.csv tmp/features.csv
python tools/missing_handler.py tmp/features.csv tmp/trades.csv tmp/nl_no_missing.csv tmp/el_no_missing.csv
python tools/backbone_runner.py tmp/nl_no_missing.csv tmp/el_no_missing.csv 0.8 1 data/nodelist_2011.csv data/edgelist_2011.csv reports