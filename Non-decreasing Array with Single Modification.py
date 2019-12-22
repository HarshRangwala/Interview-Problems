'''
class Solution(object):
    def checkPossibility(self, nums):
        modified = False
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                if modified:
                    return False
            if i>=2 and nums[i]<nums[i-2]:
                nums[i] = nums[i-1]
            modified = True
        return True
print(Solution().checkPossibility(([3,15,16,1,111,112])))
'''
import random
def nd(nums):
    counter = 0
    for i in range(1, len(nums)):
        if(nums[i]<nums[i-1]):
            try:
                nums[i]=random.randrange(nums[i-1],nums[i+1],1)
                counter = counter + 1
                break
            except:
                nums[i]=random.randrange(nums[i-1],nums[i-1]+1,1)
                counter = counter + 1
    if(counter<=1):
        return True
    return False
print(nd([3,15,16,1,3,16,112]))
