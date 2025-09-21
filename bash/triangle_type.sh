#!/bin/bash
# Bash script to classify triangle type based on three sides
# Input: three numbers from STDIN, one per line
# Output: EQUILATERAL / ISOSCELES / SCALENE
# Author: Adity

# Read sides from three separate lines
read s1
read s2
read s3

# Check triangle type
if [ "$s1" = "$s2" ] && [ "$s2" = "$s3" ]; then
    echo "EQUILATERAL"
    elif [ "$s1" = "$s2" ] || [ "$s1" = "$s3" ] || [ "$s2" = "$s3" ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
