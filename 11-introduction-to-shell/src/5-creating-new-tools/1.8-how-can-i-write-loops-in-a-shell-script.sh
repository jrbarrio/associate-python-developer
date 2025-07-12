#!/bin/bash

nano data-range.sh

# for filename in $@
# do
#     cut -d , -f 1 $filename | grep -v Date | sort | head -n 1
#     cut -d , -f 1 $filename | grep -v Date | sort | tail -n 1
# done

bash data-range.sh seasonal/*.csv
bash data-range.sh seasonal/*.csv | sort