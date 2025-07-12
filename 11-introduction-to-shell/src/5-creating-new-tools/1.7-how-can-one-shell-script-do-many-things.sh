#!/bin/bash

nano range.sh
#wc -l $@ | grep -v total | sort -n | head -n 1
#wc -l $@ | grep -v total | sort -n -r | head -n 1
bash range.sh seasonal/*.csv > range.out