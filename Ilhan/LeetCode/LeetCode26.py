class Solution(object):
    def removeDuplicates(self, nums):
        for i in reversed(nums):
            if nums.count(i) > 1:
                nums.remove(i)