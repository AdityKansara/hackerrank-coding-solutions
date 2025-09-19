# Problem: HackerRank Designer Door Mat
# 
# Explanation:
# You are given the size of a door mat with dimensions N x M (N rows and M columns).
# N is an odd natural number, and M is 3 times N.
# 
# The design rules are:
# 1. The pattern is built using "|." and "-" characters, and the word "WELCOME".
# 2. The top half of the mat has patterns with increasing "|." count.
# 3. The middle line contains "WELCOME" centered.
# 4. The bottom half mirrors the top half.
# 
# Example:
# Input: 7 21
# Output:
# ---------.|.---------
# ------.|..|..|.------
# --.|..|..|..|..|..|.--
# -------WELCOME-------
# --.|..|..|..|..|..|.--
# ------.|..|..|.------
# ---------.|.---------
#
# Constraints:
# - 5 <= N < 101
# - 15 <= M < 303
# - N is odd, M = 3*N
#
# Time Complexity: O(N)  - We loop through rows once.
# Space Complexity: O(1) - Only a few helper variables used.

def solve():
    N, M = map(int, input().split())
    design = "WELCOME"
    pattern = ".|."
    character = "-"
    counter = 1
    middle_line = (N - 1) // 2

    for i in range(N):
        if i == middle_line:
            print(design.center(M, character))
        elif i < middle_line:
            print((pattern * counter).center(M, character))
            counter += 2
        else:
            counter -= 2
            print((pattern * counter).center(M, character))


if __name__ == "__main__":
    solve()
