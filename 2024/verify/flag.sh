#!/bin/bash

directory="home/ctf-player/drop-in/files"
checksum="3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4"

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  exit 1
fi

# Loop through files in the target directory
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    sha256value=$(cat $file | sha256sum | cut -d " " -f 1)
    if [ $sha256value == $checksum ]; then
    	echo "checksum_value: $sha256value"
    	echo "file_location: $file"
    	echo "Decrypting...."
      openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$file" -k picoCTF
      # ./home/ctf-player/drop-in/decrypt.sh $file
    fi
  fi
done

