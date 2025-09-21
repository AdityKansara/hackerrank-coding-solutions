# #Problem - Capitalize!
# Problem solved by Adity
# Given a string, capitalize the first letter of each word while keeping the rest unchanged.
# Example:
# Input:  "hello world"
# Output: "Hello World"
#
# Approach:
# 1. Split the string into words by spaces.
# 2. For each word, convert the first character to uppercase and append the rest of the word.
# 3. Join the words back with spaces to form the final string.
#
# Time Complexity: O(n) - where n is the length of the string (we traverse each character once).
# Space Complexity: O(n) - storing the words list and the transformed string.


def solve(s):
    words = s.split(" ")
    for i in range(len(words)):
        if words[i]:
            words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)


if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)
