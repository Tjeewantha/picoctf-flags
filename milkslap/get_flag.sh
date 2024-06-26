#!/bin/bash

file=$1
result=$(RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg $file | cut -d ':' -f2 | sort | uniq | sed 1,4d | sed '1!d' | cut -c 3- | rev | cut -c 4- | rev)

echo $result


