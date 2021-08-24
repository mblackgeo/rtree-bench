# rtree-bench
Benchmarking rtree vs pygeos spatial indexing using Geopandas. Experimental PyGEOS support was added in Geopandas 0.9.0 and underneath uses a pygeos' STRtree (sort-tile-recursive rtree) which can speed up the querying process of an rtree compared to using the python `rtree` support (which wraps `libspatialindex`).

To run:

```shell
./build.sh && ./run.sh
```

Results:

```
============================================================================= test session starts =============================================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
benchmark: 3.4.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /
plugins: benchmark-3.4.1
collected 2 items

bench.py ..                                                                                                                                                             [100%]


------------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------------
Name (time in ms)                  Min                   Max                  Mean             StdDev                Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_bench_sjoin_pygeos       754.0034 (1.0)        799.2969 (1.0)        773.9812 (1.0)      22.6748 (1.0)        761.7404 (1.0)       42.1178 (1.0)           2;0  1.2920 (1.0)           5           1
test_bench_sjoin            9,597.6096 (12.73)    9,770.6800 (12.22)    9,691.9209 (12.52)    67.8177 (2.99)     9,708.2128 (12.74)    101.6873 (2.41)          2;0  0.1032 (0.08)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================ 2 passed, 21000 warnings in 75.09s (0:01:15) =================================================================
```