/*
In this problem, I have to use two pointer and sliding window.
it is finding Minimum size subarray, so required high value of indecies.
the two pointers are start and end, starting side to side locations.
then, if a pointer is lower then another pointer, move the lower pointer.
this problem's key point is that subarray is a contiguous sequence.
*/

class Solution {
    public:
        int minSubArrayLen(int target, vector<int>& nums) {
            int sum = 0;
            vector<int> sub_ary; 
            int min_size = nums.size();
            int sub_size;
            int sub_sum = 0;
    
            if (accumulate(nums.begin(), nums.end(), 0) < target) {
                return 0;
            }
    
            for (int i = 0; i < nums.size(); i++) {
                sub_ary.push_back(nums[i]);
                //because of accumulate function, time limit exceeded occurred
                //sub_sum = accumulate(sub_ary.begin(), sub_ary.end(), 0);
                sub_sum += nums[i];
    
                while (sub_sum >= target) {
                    sub_size = sub_ary.size();
                    if(sub_size < min_size) {
                        min_size = sub_size;
                    }
                    sub_sum -= sub_ary.front();
                    sub_ary.erase(sub_ary.begin());
                    //sub_sum = accumulate(sub_ary.begin(), sub_ary.end(), 0);
                }
            }
    
            return min_size;
        }
    };