#!/bin/bash

while read file_line; do
    echo "$file_line"
done < "$1"
