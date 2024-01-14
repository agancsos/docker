###############################################################################
# Name        : Makefile                                                      #
# Author      : Abel Gancsos                                                  #
# Version     : v. 1.0.0.0                                                    #
# Description : Helps bootstrap this container.                               #
###############################################################################
.DEFAULT_GOAL := build
IMAGE_NAME    := $(shell basename "$$PWD" )

build:
	which docker
	docker build --platform linux/x86_64 -t $(IMAGE_NAME):latest .

run:
	which docker
	docker run -d --platform linux/x86_64 -p 9991:9990 -p 8081:8080 --name $(name) --privileged -t $(IMAGE_NAME):latest

shutdown:
	which docker
	docker stop $(name); docker rm $(name)

