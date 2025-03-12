/*
이 문제는 투 포인터를 활용해서 풀면 더 쉽게 풀 수 있을 거 같다.
1. 첫번째 포인터를 배열의 맨 앞에 위치 시키고, 두번째 포인터를 그 다음 포인터에 위치 시킨다음, target이 될 때까지 두번째 포인터를 이동 시킨다. 이 방법은 최악의 경우 시간 복잡도 n이 소요될 수 있다.
2. 첫번째 포인터를 배열의 맨 앞에 위치시키고, 두번째 포인터를 맨 뒤로 이동 시킨다음, target보다 두 번째 포인터가 클 경우 점점 앞으로 이동하게 한다. 하지만 이 경우도 최악의 경우 n 만큼 소요될 수 있다.

일단, 제일 편한 
*/

class Solution {
    public:
        vector<int> twoSum(vector<int>& numbers, int target) {
            vector<int> result;
            int a = 0;
            int b = numbers.size()-1;
    
            for (int i = 0; i < numbers.size(); i++) {
                if (target == numbers[a] + numbers[b]) {
                    result.push_back(a+1);
                    result.push_back(b+1);
                    return result;
                } else if (target < numbers[a] + numbers[b]) {
                    b--;
                } else {
                    a++;
                }
            }
            return result;
        }
    };