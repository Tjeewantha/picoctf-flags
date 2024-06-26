#!/bin/bash

file=$1
command=$(tshark -n -r $file -q -z follow,udp,ascii,6 | sed '1,7d' | sed '$d' | tr -d '\n' | tr -d '1')
echo $command
