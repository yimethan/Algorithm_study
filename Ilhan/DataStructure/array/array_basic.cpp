#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    vector<int> arr = {4, 2, 1, 5, 7, 8 ,10, 11};
    
    sort(arr.begin(), arr.end());

    cout << "정렬된 배열: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "\n";
    return 0;
}