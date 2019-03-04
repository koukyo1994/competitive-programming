IMAGE := competitive:1.0

build: Dockerfile
	docker build -t ${IMAGE} .

env:
	docker run -v `pwd`:/app -it ${IMAGE} /bin/bash
