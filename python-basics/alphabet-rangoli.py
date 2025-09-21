# #Problem - Alphabet Rangoli
# Problem solved by Adity
# Given an integer size N, print an alphabet rangoli of size N.
#
# An alphabet rangoli is a symmetric pattern of English alphabets
# arranged in the form of a rangoli design. The center contains the
# Nth alphabet, and the design expands outwards with hyphens (-) as
# fillers.
#
# Example (N = 3):
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# Approach:
# 1. Calculate the total width = 4*N - 3 and height = 2*N - 1.
# 2. Use ASCII value of 'a' (97) as the starting point.
# 3. Build rows by first appending descending characters then ascending characters.
# 4. Use str.center(width, '-') to align each row symmetrically.
# 5. Print the upper half first (reversed), then the lower half.
#
# Time Complexity: O(N^2) - nested loops to build each row.
# Space Complexity: O(N^2) - storing and printing rows.


def print_rangoli(size):
    startValue = 97
    width = (4 * size) - 3
    height = (2 * size) - 1

    for i in range(size - 1, 0, -1):
        row = ""

        for j in range(size - 1, i, -1):
            row += chr(startValue + j) + "-"

        for j in range(i, size):
            row += chr(startValue + j)
            if j != size - 1:
                row += "-"

        print(row.center(width, "-"))

    for i in range(size):
        row = ""

        for j in range(size - 1, i, -1):
            row += chr(startValue + j) + "-"

        for j in range(i, size):
            row += chr(startValue + j)
            if j != size - 1:
                row += "-"

        print(row.center(width, "-"))


if __name__ == "__main__":
    n = int(input().strip())
    print_rangoli(n)
