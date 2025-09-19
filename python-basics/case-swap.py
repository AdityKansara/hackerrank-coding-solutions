# Problem: HackerRank - Swap Case
#
# Explanation:
# Given a string, you need to swap the case of all its characters.
# - All lowercase letters should become uppercase.
# - All uppercase letters should become lowercase.
#
# Example:
# Input: "HackerRank.com presents 'Pythonist 2'."
# Output: "hACKERrANK.COM PRESENTS 'pYTHONIST 2'."
#
# Constraints:
# - 0 < len(s) <= 1000
#
# Time Complexity: O(n) - We iterate over each character once.
# Space Complexity: O(1) - Only a few helper variables are used.

def swap_case(s):
    a = ''
    for ch in s:
        ch = ch.lower() if ch.isupper() else ch.upper()
        a = a + ch
    return a


def solve():
    s = input()
    result = swap_case(s)
    print(result)


if __name__ == "__main__":
    solve()
