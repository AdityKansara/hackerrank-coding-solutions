#!/bin/bash
# Bash script to read a single character from STDIN
# and print YES if Y/y or NO if N/n
# Author: Adity

# Read exactly one character
read -n 1 char

# Check character and display output
case "$char" in
    [Yy]) echo "YES" ;;
    [Nn]) echo "NO" ;;
esac
