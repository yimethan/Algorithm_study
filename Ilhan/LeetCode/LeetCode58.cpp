/*
이 문제는 문장의 마지막 단어의 길이를 알면 되는 문제이다.
띄어쓰기를 기준으로 단어를 나누고 가장 마지막 단어만 추출하면 될 것 이다.
*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream iss(s);

        string word;

        while (iss >> word) {}

        return word.length();
    }
};