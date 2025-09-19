# The Minion Game
# A word game between two players, Kevin and Stuart.
# - Kevin scores points for substrings starting with vowels.
# - Stuart scores points for substrings starting with consonants.
# Instead of generating all substrings (which is slow), the score is calculated
# by counting how many substrings can be formed starting from each position.
#
# Example:
# Input:  BANANA
# Output: Stuart 12
# Explanation:
#   Stuart gets points for substrings starting with B, N, N = 12
#   Kevin gets points for substrings starting with A, A, A = 9
#   Stuart wins.

def minion_game(string):
    vowels = "AEIOU"
    kevin = stuart = 0
    length = len(string)

    for i in range(length):
        if string[i].upper() in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
    
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)