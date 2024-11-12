
# // Time Complexity :
# // Space Complexity :
# // Did this code successfully run on Leetcode :
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        r = m-1
        c = 0

        while (r >= 0 and c < n):
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                r -=1
            else:
                c+=1

        return False     