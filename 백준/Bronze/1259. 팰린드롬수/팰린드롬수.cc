#include <iostream>
using namespace std;

int main(){
    string num;
    string result;

    while(true){
        cin >> num;
        result = "yes";

        if(num == "0") break;
        else{
            for(int i=0; i < num.length()/2; i++){
                if(num[i] != num[num.length()-1-i]) result = "no";
            }
        }

        cout << result << endl;
    }
}