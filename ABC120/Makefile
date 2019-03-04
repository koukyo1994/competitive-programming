CXX := g++
ACPP := src/a.cpp
BCPP := src/b.cpp
CCPP := src/c.cpp
DCPP := src/d.cpp

CFLAGS := -O2 -Wall -std=c++11 -DDEBUG
A := build/a.out
B := build/b.out
C := build/c.out
D := build/d.out

prob-a: ${A}

prob-b: ${B}

prob-c: ${C}

prob-d: ${D}

${A}: ${ACPP}
	${CXX} ${CFLAGS} ${ACPP} -o ${A}

${B}: ${BCPP}
	${CXX} ${CFLAGS} ${BCPP} -o ${B}

${C}: ${CCPP}
	${CXX} ${CFLAGS} ${CCPP} -o ${C}

${D}: ${DCPP}
	${CXX} ${CFLAGS} ${DCPP} -o ${D}
