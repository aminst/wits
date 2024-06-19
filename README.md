# ERGM on WITS

This repository aims to use the dataset provided by World Integrated Trade Solution (WITS) to model the trade network between countries based on the structural statistics available and also nodal information on countries. To do so, we use the Exponential Random Graph Models.  
[Link to the Published Article](https://appliednetsci.springeropen.com/articles/10.1007/s41109-022-00479-7)

## Datasets
We have provided all the data files used in the study in the `data` directory. If you wish to regenerate these files you can use the `data_pipeline.sh` script to do so. The `initial_trades.csv` is the downloaded trades from the WITS website.

## Cite
```
@article{setayesh2022analysis,
  title={Analysis of the global trade network using exponential random graph models},
  author={Setayesh, Amin and Sourati Hassan Zadeh, Zhivar and Bahrak, Behnam},
  journal={Applied Network Science},
  volume={7},
  number={1},
  pages={1--19},
  year={2022},
  publisher={SpringerOpen}
}
```
