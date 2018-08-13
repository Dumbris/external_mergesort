The python implementation of an external sort for sorting large text files. This script consumes only 8Mb RAM to sort 26G file.

== Generate csv file
FILENAME=/media/data/test2.csv python3 generator.py

== Run sorting script
INFILE=/media/data/test2.csv OUTFILE=/media/data/test2_sorted.csv python3 external_sort.py
python3 external_sort.py

== Create limit for cgroup (Linux)
./create_cgroup.sh

== Run script with limited memory
sudo cgexec -g memory:myGroup2 INFILE=/media/data/test2.csv OUTFILE=/media/data/test2_sorted.csv python3 external_sort.py

== Run unit tests
python3 -m unittest
