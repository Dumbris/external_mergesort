#!/bin/sh

export INFILE=/media/data/test200.csv
export OUTFILE=/media/data/test200_sorted.csv
#sudo cgexec -g memory:myGroup200 python3
#valgrind --tool=massif python3 external_sort.py
python3 external_sort.py