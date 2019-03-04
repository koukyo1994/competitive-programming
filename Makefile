IMAGE := competitive:1.0
CONTEST := abc120

build: Dockerfile
	docker build -t ${IMAGE} .

env:
	docker run -v `pwd`:/app -it ${IMAGE} /bin/bash

retrieve:
	./dirmake.sh `echo ${CONTEST} | tr a-z A-Z`
	python tools/retriever.py ${CONTEST}
