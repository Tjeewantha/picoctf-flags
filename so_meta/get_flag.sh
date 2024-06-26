#!/bin/bash

file=$1
command=$(exiftool pico_img.png | cut -d ':' -f2 | uniq | sed '1,24d' | sed '1!d')
echo $command
