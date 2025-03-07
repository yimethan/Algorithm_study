'''
이 문제는 k 만큼 가장 마지막 요소를 맨 앞으로 보내면 되는 문제이다.
원형 큐 문제로 볼 수 있다.
하지만 그렇게 풀기엔 귀찮기 때문에 deque를 사용하거나 간단하게 해결해보겠다.
'''
from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        dq = deque(nums)
        dq.rotate(k)
        nums[:] = list(dq)
        print(nums)