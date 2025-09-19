# #Polar Coordinates Problem - HackerRank
# Problem solved by Adity
# Time Complexity: O(1) - Direct math operations
# Space Complexity: O(1) - No extra memory used

import cmath

z = complex(input().strip())
print(abs(z))         # magnitude
print(cmath.phase(z)) # phase angle
