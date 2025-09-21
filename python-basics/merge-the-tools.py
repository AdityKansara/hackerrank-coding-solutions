# Merge the Tools!
# Problem Statement:
# Given a string S and an integer K, split the string into substrings of length K.
# For each substring, remove any duplicate characters while preserving the order.
# Then print the modified substring.
#
# Example:
# Input:
#     AABCAAADA
#     3
# Output:
#     AB
#     CA
#     AD
#
# Explanation:
# - Split "AABCAAADA" into equal parts of length 3 → ["AAB", "CAA", "ADA"]
# - Remove duplicates while preserving order:
#     "AAB" → "AB"
#     "CAA" → "CA"
#     "ADA" → "AD"


def merge_the_tools(string, k):
    a = [string[i : i + k] for i in range(0, len(string), k)]

    for i in a:
        print("".join(dict.fromkeys(i)))


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
