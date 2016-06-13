default: all

all: a.o

a.o:
	gcc a.c

install: a.o
	cp a.c INSTALL_DIR
