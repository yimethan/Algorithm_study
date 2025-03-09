#include <iostream>
#include <string>
#include <algorithm>


using namespace std;
int main() {
    string str = "Helli World!";
    
    reverse(str.begin(), str.end());

    cout << "reverse string: " << str << "\n";
    return 0;
}