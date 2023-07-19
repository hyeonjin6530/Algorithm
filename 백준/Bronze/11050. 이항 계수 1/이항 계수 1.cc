#include <iostream>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int result = 1;

    if(k < 0 or k > n) result = 0;
    else{
        for(int i=1; i<n+1; i++){
            result *= i;
        }
        for(int i=1; i<k+1; i++){
            result /= i;
        }
        for(int i=1; i<n-k+1; i++){
            result /= i;
        }
    }

    cout << result << endl;
}