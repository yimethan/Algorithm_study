class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 1
        for i in range(1, len(nums)):
            if nums[check-1] != nums[i]:
                nums[check] = nums[i]
                check += 1
        return check
    
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         check = []
#         for i in range(len(nums)):
#             if nums[i] not in check:
#                 check.append(nums[i])
#         for i in range(len(check)):
#             nums[i] = check[i]
#         return len(check)