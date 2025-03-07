'''
그러니까, 이 문제는 non-decreasing 순서로 정렬된 배열에서 최대 2번까지만 나타나게 변경해야 한다.
그리고 return으로 배열의 남은 인덱스 수인 k를 반환하면 된다는건가?
그리고, 중복을 제거한 남은 자리에 _ 언더라인을 채워넣고, 맨 뒤로 보내야한다는건가?
일단 순서는
1. 각 요소 중에서 3번 이상 나타난 요소를 찾고 자리도 찾는다.
2. 그 요소 자리에 _를 넣는다.
3. 그리고 정렬을 통해 _ 를 맨 뒤로 보낸다.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        n = nums[-1]
        # print("first nums: ", nums)
        for i in range((len(nums)-1), -1, -1):
            # print(f"n: {n} nums[{i}]: {nums[i]}")
            if n == nums[i]:
                count += 1
                # print(f"n == num[{i}], count: {count}")
                if count >= 3:
                    k = nums.pop(i)
                    # print("poped :", k)
            else:
                count = 1
                n = nums[i]
                # print(f"n != num[{i}] n: {n} count: {count}")

        print(nums)