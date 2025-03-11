/*
이 문제는 하위 시퀀스를 판단하는 문제로, t를 처음과 끝에서 출발해서 t.size() / 2만큼 반복해서 보는데,
s가 비워질때까지 한다.
*/

class Solution {
    public:
        bool isSubsequence(string s, string t) {
            queue<char> q;
            for (char c : s) {
                q.push(c);
            }
            for(int i = 0; i < t.size(); i++) {
                if(q.front() == t[i]) {
                    q.pop();
                }
            }
            if(q.empty()) {
                return true;
            } else {
                return false;
            }
        }
    };