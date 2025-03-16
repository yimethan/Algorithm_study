/*
In this problem, not only the value of each index(height), but also the spacing between indexes(width) is important too.
So, I can approch two pointer in this problem at first.
1. two pointer start at the same position.
2. two pointer start at diffient position that both end positions.
but, Usually option 2 is finding answer faster than option 1. because option 2's spacing between is wide.

I ended up using gpt hint: 

The key idea is that the area is limited by the shorter line.
If you move the pointer corresponding to the taller line inward, you won’t increase the minimum height, so the area can’t get larger.
Instead, move the pointer with the smaller height inwards to try to find a taller line that might increase the area.
Repeat Until the Pointers Meet:

Continue this process until the left pointer meets the right pointer.
*/

class Solution {
    public:
        int maxArea(vector<int>& height) {
            int start = 0;
            int end = height.size() - 1;
            int max_width = (end - start) * (min(height[start], height[end]));
    
            while(end != start) {
                int new_width = (end - start) * (min(height[start], height[end]));
    
                if (max_width < new_width) {
                    max_width = new_width;
                }
                if (height[start] > height[end]) {
                    end--;
                }
                else {
                    start++;
                }
            }
    
            return max_width;
        }
    };