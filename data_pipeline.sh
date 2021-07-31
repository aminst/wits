YEAR=2011

python tools/trade_cleaner.py data/$YEAR/initial_trades.csv tmp/$YEAR/trades.csv
python tools/feature_merger.py data/$YEAR/features/countries.csv data/$YEAR/features/gdp.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/inflation.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/gdp_growth.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/colonization.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/geo_cepii.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/population.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/gdp_per_capita.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/life_expectancy.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/gni_atlas.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/agriculture_forestry_fishing_of_gdp.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/industry_of_gdp.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/merchandise_of_gdp.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/net_barrier_of_trade.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/foreign_direct_investment_inflows.csv tmp/$YEAR/features.csv
python tools/feature_merger.py tmp/$YEAR/features.csv data/$YEAR/features/happiness.csv tmp/$YEAR/features.csv
python tools/missing_handler.py tmp/$YEAR/features.csv tmp/$YEAR/trades.csv tmp/$YEAR/nl_no_missing.csv tmp/$YEAR/el_no_missing.csv
python tools/backbone_runner.py tmp/$YEAR/nl_no_missing.csv tmp/$YEAR/el_no_missing.csv 0.8 1 data/$YEAR/nodelist.csv data/$YEAR/edgelist.csv reports/$YEAR
python tools/dist_modifier.py data/$YEAR/nodelist.csv data/$YEAR/features/dist_cepii.csv data/$YEAR/features/dist.csv
python tools/diplomatic_exchange_modifier.py data/$YEAR/features/diplomatic_exchange.csv info/country_names.txt data/$YEAR/nodelist.csv data/$YEAR/features/dip_exhange_clean.csv