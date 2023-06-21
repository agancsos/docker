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
	docker build -t $(IMAGE_NAME):latest .

run:
	which docker
	docker run -d --name $(name) -p 1194:1194/udp --privileged --cap-add=NET_ADMIN -t $(IMAGE_NAME):latest

shutdown:
	which docker
	docker stop $(name); docker rm $(name)
