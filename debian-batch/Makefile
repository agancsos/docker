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
    docker run -d --platform linux/x86_64 --name $(name) --privileged -p 3270:3270 -p 3278:3278 -p 8038:8038 -p 3505:3505 -t $(IMAGE_NAME):latest
    sleep 130

shutdown:
    which docker
    docker stop $(name); docker rm $(name)
