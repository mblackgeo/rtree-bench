import random

import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon


def create_data():
    random.seed(0)
    np.random.seed(0)

    triangles = gpd.GeoSeries([Polygon([(random.random(), random.random()) for _ in range(3)]) for _ in range(1000)])
    points = gpd.GeoSeries([Point(x, y) for x, y in zip(np.random.random(10000), np.random.random(10000))])

    df1 = gpd.GeoDataFrame({'val1': np.random.randn(len(triangles)), 'geometry': triangles})
    df2 = gpd.GeoDataFrame({'val1': np.random.randn(len(points)), 'geometry': points})

    return df1, df2


def bench_sjoin(use_pygeos: bool = False):
    gpd.options.use_pygeos = use_pygeos
    df1, df2 = create_data()
    gpd.sjoin(df1, df2)


def test_bench_sjoin(benchmark):
    benchmark(bench_sjoin, use_pygeos=False)


def test_bench_sjoin_pygeos(benchmark):
    benchmark(bench_sjoin, use_pygeos=True)
