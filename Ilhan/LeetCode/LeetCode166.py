'''
이 문제는 어떻게 풀 수 있을까?
먼저, nums의 길이 n, n / 2 보다 많아야 Majority Elemnet에 선정된다.
그렇다면, 배열을 돌면서 각 요소를 Count하고, 그 중에서 n / 2 보다 높은 Elements를 return하면 되지 않을까?
얘는 어차피 해봤자, 최대 n개의 요소를 갖는다.
여기에서, 각 요소마다 count하는 게 굉장히 중요해 보이는데, 이걸 어떻게 할건지가 관건이다.
여기에서 만약에 정렬을 쓴다면?
정렬을 하면 좀 더 쉽게 풀리지 않을까?
정렬을 해서, [2,2,1,1,1,2,2] 였던 걸 [1,1,1,2,2,2,2]로 만들어 주면
일단 같은 요소끼리는 붙으니까, 
if 다른 요소 나오면 그때 부턴 다른 요소
else 같은 요소
이렇게 조건을 세워서, Count를 해보면 모든 요소를 count할 수 있지 않을까
아니면, 더 좋은 방법은 빈도수를 기준으로 정렬을 하는 건데, 그게 어떻게 가능한지는 모르겠다.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        a = nums[0]
        count = 0
        for i in nums:
            if a == i:
                #같은 요소
                count += 1
                print ("same element: ", a, " count: ", count)

                if count > (len(nums) / 2):
                    print("count > (nums.length / 2): ", count)
                    return i
            else:
                #다른 요소
                a = i
                count = 1
                print ("changed element: ", a, " count: ", count)
        