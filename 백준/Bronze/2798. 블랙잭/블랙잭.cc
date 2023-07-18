#include <iostream>
using namespace std;

int main(){
    int c_num, num;
    cin >> c_num >> num;

    int card;
    int card_list[c_num] = {};

    for(int i=0; i<c_num; i++){
        cin >> card;
        card_list[i] = card;
    }

    int sum, result=0;

    for(int i=0; i<c_num; i++){
        for(int j=i+1; j<c_num; j++){
            for(int k=j+1; k<c_num; k++){
                sum = card_list[i]+card_list[j]+card_list[k];
                if(result < sum && sum <= num) result = sum;
            }
        }
    }

    cout << result << endl;
}