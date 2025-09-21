# #No Idea Problem - HackerRank
# Problem solved by Adity
# Time Complexity: O(n) - loop through array
# Space Complexity: O(n) - store sets A and B

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    if x in B:
        happiness -= 1

print(happiness)
