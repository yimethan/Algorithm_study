class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cnt = {}

        for i in nums1[:m]:
            if i in cnt.keys():
                cnt[i] += 1
            else:
                cnt[i] = 1
        for i in nums2:
            if i in cnt.keys():
                cnt[i]+= 1
            else:
                cnt[i] = 1
                
        cnt = dict(sorted(cnt.items()))

        idx = 0
        for i in cnt.keys():
            for _ in range(cnt[i]):
                nums1[idx] = i
                idx += 1
