#!/bin/sh

cp seasonal/spring.csv seasonal/summer.csv ~
grep -h -v Tooth spring.csv summer.csv > temp.csv
history | tail -n 3 > steps.txt