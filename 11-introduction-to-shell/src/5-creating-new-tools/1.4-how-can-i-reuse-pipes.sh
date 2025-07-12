#!/bin/bash

nano teeth.sh
#cut -d , -f 1 seasonal/*.csv | grep -v Tooth | sort | uniq -c
bash teeth.sh > teeth.out
cat teeth.out