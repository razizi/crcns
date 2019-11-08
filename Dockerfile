FROM continuumio/anaconda3:4.6.14

RUN conda install --yes \
    nomkl \
    dask==1.2.2 \
    numpy==1.16.3 \
    pandas==0.24.2 \
    tini==0.18.0 \
    tensorflow==2.0.0

ENTRYPOINT ["tini", "-g", "--"]

RUN free -m