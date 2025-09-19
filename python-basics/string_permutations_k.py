# #Problem - String Permutations of Size k
# Problem solved by Adity
# Given a string and an integer k, generate all possible permutations
# of size k of the string in lexicographically sorted order.
# Time Complexity: O(n! / (n-k)!) - permutations generation
# Space Complexity: O(n) - storing characters for each permutation

from itertools import permutations

s = input()
parts = s.split(" ")
s = sorted(parts[0])
k = int(parts[1])

for p in permutations(s, k):
    print("".join(p))