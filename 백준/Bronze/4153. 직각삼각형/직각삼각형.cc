#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    int sum;
    int num[3] = {};

    while(true){
        sum = 0;
        for (int i=0; i<3; i++){
            cin >> n;
            num[i] = n;
            sum += n;
        }
        if(sum == 0) break;
        else{
            sort(num, num+3);
            if(num[0]*num[0] + num[1]*num[1] == num[2]*num[2]) cout << "right" << endl;
            else cout << "wrong" << endl;
        }
    }
}