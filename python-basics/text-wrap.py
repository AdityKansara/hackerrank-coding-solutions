# #Problem - Text Wrap
# Problem solved by Adity
# Given a string and a maximum width, wrap the string into a paragraph
# so that each line contains at most the given width characters.
#
# Example:
# Input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
#
# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
#
# Approach:
# 1. Use textwrap.wrap() to split the string into chunks of size max_width.
# 2. Concatenate each chunk with a newline character.
# 3. Return the formatted string.
#
# Time Complexity: O(n) - where n is the length of the string.
# Space Complexity: O(n) - for storing the wrapped lines.

import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)
    ans = ""
    for item in a:
        ans = ans + item + "\n"
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
