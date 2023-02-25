###############################################################################
# Name        : Makefile                                                      #
# Author      : Abel Gancsos                                                  #
# Description : Helps build and run z/OS Docker container.                    #
###############################################################################
.DEFAULT_GOAL := build

build:
	docker build --platform linux/x86_64 -t herc-zos .

run:
	docker run --platform linux/x86_64 -p 3270:3270 -p 8038:8038 -p 3278:3278 --name $(name) -d -t herc-zos
	sleep 190

clean:
	docker stop $(name)
	docker rm $(name)

find:
	docker ps | grep $(name); exit 0
