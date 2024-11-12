
# // Time Complexity :
# // Space Complexity :
# // Did this code successfully run on Leetcode :
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach

class Solution:
    def removeDuplicates(self, nums: List[int]):
        # hmap = {}
        # dont use hmap it is wrong use algorithms
        n =len(nums)
        s,f = 0,0
        target = 2
        count = 0
        while f < n:
            if f > 0 and nums[f] == nums[f-1]:
                count +=1
            else:
                count = 1
            
            if count <= target:
                nums[s] = nums[f]
                s+=1
            f+=1
        return s