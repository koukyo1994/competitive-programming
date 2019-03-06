FROM ubuntu:16.04
RUN apt-get update &&\
    apt-get install -yq software-properties-common

RUN add-apt-repository universe &&\
    apt-get update &&\
    apt-get install -yq g++ libboost-all-dev cmake make gdb &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*
RUN mkdir /app
WORKDIR /app

CMD ["/bin/bash"]
