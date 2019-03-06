IMAGE := competitive:1.0
CONTEST := abc120

build: Dockerfile
	docker build -t ${IMAGE} .

env:
	docker run -v `pwd`:/app -it ${IMAGE} /bin/bash

retrieve:
	./dirmake.sh `echo ${CONTEST} | tr a-z A-Z`
	python tools/retriever.py ${CONTEST}

debug:
	docker run -v `pwd`:/app -i -t --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" ${IMAGE} /bin/bash
