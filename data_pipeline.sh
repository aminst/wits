python tools/trade_cleaner.py data/Trade_BEH0_2011_Export_2020Jul10.csv tmp/trades.csv
python tools/feature_merger.py data/features/countries.csv data/features/gdp_2011.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/inflation_2011.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/gdp_growth_2011.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/colonization.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/geo_cepii.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/population.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/gdp_per_capita.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/life_expectancy.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/gni_atlas.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/agriculture_forestry_fishing_of_gdp.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/industry_of_gdp.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/merchandise_of_gdp.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/net_barrier_of_trade.csv tmp/features.csv
python tools/feature_merger.py tmp/features.csv data/features/foreign_direct_investment_inflows.csv tmp/features.csv
python tools/missing_handler.py tmp/features.csv tmp/trades.csv tmp/nl_no_missing.csv tmp/el_no_missing.csv
python tools/backbone_runner.py tmp/nl_no_missing.csv tmp/el_no_missing.csv 0.8 1 data/nodelist_2011.csv data/edgelist_2011.csv reports
python tools/dist_modifier.py data/nodelist_2011.csv data/features/dist_cepii.csv data/features/dist.csv
python tools/diplomatic_exchange_modifier.py data/features/diplomatic_exchange.csv info/country_names.txt data/nodelist_2011.csv data/features/dip_exhange_clean.csv