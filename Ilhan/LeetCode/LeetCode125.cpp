/*
이 문제는 Palindrome인지 판단하는 문제이다.
일단 모든 문자를 소문자로 변경하고, 띄어쓰기, 숫자 등을 전부 제거해서 문자 character만 남긴다.
그 후에, 맨 왼쪽과 오른쪽에서 하나씩 접근하면서, 문자가 같으면 ture
*/

class Solution {
    public:
        bool isPalindrome(string s) {
            for(int i = s.size()-1; i >= 0; i--) {
                if(!isalnum(s[i])) {
                    s.erase(i, 1);
                } else {
                    s[i] = tolower(s[i]);
                }
            }
    
            for(int i = 0; i < s.size()/2; i++) {
                char a, b;
                a = s[i];
                b = s[(s.size()-1) - i];
                if (a != b) {
                    return false;
                }
            }
            return true;
        }
    };