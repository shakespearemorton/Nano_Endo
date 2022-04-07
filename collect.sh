#!/bin/bash

res="RFRAC"
res2="REPSILON"

for val in {0..2..1}
do
    rm -r $val
    mkdir $val
    cd $val
    for val2 in {0..2..1}
    do
        mkdir $val2
        cd $val2
        cp ../../* .
        sed -e "s/$res/$val/" starter.py > start1.py
        sed -e "s/$res2/$val2/" start1.py > start.py
        python start.py
        qsub subfile.pbs
        cd ..
    done
    cd ..
done
