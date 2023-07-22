#include <iostream>
using namespace std;

int main(){
    int up, down, distance;
    cin >> up >> down >> distance;

    int count = 1;
    count += (distance-up)/(up-down);

    if((distance-up)%(up-down) != 0)
        count++;
    if(up >= distance)
        cout << "1";
    else
        cout << count;
}