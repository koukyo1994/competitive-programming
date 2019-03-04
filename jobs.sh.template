for f in 0 1 2; do \
  ./$1 < cases/$2/$f/input.txt | xargs > cases/$2/$f/output.txt; \
  diff cases/$2/$f/output.txt cases/$2/$f/answer.txt; \
done
