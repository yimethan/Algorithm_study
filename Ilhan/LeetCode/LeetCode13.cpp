/*
이 문제 같은 경우에는 로마 숫자가 주어지면, 이걸 정수로 변환해야 하는 문제이다.
일단, 각 문자마다 매칭되는 값들을 딕셔너리 형태로 만들면 좋을 거 같다.
그리고, s에 한글자씩 나눠서 처리하거나, s를 map과 매칭해서 값이 나오면 거기만 삭제하거나,

*/

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        cin.tie(0); cout.tie(0);
        ios_base::sync_with_stdio(false);

        map<string, int> romanMap;
        romanMap["I"] = 1;
        romanMap["V"] = 5;
        romanMap["X"] = 10;
        romanMap["L"] = 50;
        romanMap["C"] = 100;
        romanMap["D"] = 500;
        romanMap["M"] = 1000;
        romanMap["IV"] = 4;
        romanMap["IX"] = 9;
        romanMap["XL"] = 40;
        romanMap["XC"] = 90;
        romanMap["CD"] = 400;
        romanMap["CM"] = 900;

        int sum = 0;
        while (s.length() > 0) {
            if (s.length() >= 2) {
                string key = s.substr(0, 2);
                auto n = romanMap.find(key);
                if (n != romanMap.end()) {
                    int v = n -> second;
                    // cout << "find key 2: " << v << "\n";
                    sum += v;
                    s.erase(0, 2);
                    continue;
                }
            }

            string key = s.substr(0, 1);
            auto n = romanMap.find(key);
            int v = n -> second;
            // cout << "find key 1: " << v << "\n";
            sum += v;
            s.erase(0, 1);
        }

        return sum;
    }
};