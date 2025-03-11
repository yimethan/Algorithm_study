/*
이 문제는 k 번째 큰 요소를 찾는 문제로, heap을 사용하면 정렬과 k 번째 큰 요소를 찾을 때 도움이 될 것이라고 생각한다.
일단 최대 힙으로 배열을 만들고, 힙 정렬로 배열을 정렬한 후에, k 번째 큰 요소를 빼면 될 것이다.
*/

#include <algorithm>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        make_heap(nums.begin(), nums.end());
        sort_heap(nums.begin(), nums.end());

        return nums[nums.size() - k];
    }
};