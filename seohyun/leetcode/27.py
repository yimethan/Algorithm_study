class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        neq = []
        for i in range(len(nums)):
            if nums[i] != val:
                neq.append(nums[i])
        i = 0
        for n in neq:
            nums[i] = n
            i += 1
        return i