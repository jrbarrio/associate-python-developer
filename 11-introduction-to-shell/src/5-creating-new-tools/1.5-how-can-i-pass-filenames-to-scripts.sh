#!/bin/bash

nano cont-records.sh
#tail -q -n +2 $@ | wc -l
bash cont-records.sh seasonal/*.csv > num-records.out