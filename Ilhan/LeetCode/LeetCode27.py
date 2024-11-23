class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)

        k = len(nums)
        return k