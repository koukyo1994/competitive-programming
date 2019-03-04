if [ ! -d $1 ]; then \
  mkdir $1; \
  cp Makefile.template $1/Makefile; \
  mkdir $1/src $1/build $1/cases; \
  touch $1/build/.keep $1/cases/.keep; \
  for f in a.cpp b.cpp c.cpp d.cpp; do \
    touch $1/src/$f; \
  done; \
fi
