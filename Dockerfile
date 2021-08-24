FROM continuumio/miniconda3

RUN conda install -c conda-forge gdal proj libspatialindex pygeos pandas fiona shapely pyproj rtree geopandas
RUN pip install --no-cache-dir pytest pytest-benchmark

COPY bench.py /bench.py
CMD pytest bench.py --disable-warnings