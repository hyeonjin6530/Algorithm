#include <iostream>
using namespace std;

int main(){
    string words;
    int time = 0;

    cin >> words;

    for (int i=0; i<words.length(); i++){
        time += 2;
        if(words[i] == 'A' || words[i] == 'B' || words[i] == 'C') time += 1;
        else if(words[i] == 'D' || words[i] == 'E' || words[i] == 'F') time += 2;
        else if(words[i] == 'G' || words[i] == 'H' || words[i] == 'I') time += 3;
        else if(words[i] == 'J' || words[i] == 'K' || words[i] == 'L') time += 4;
        else if(words[i] == 'M' || words[i] == 'N' || words[i] == 'O') time += 5;
        else if(words[i] == 'P' || words[i] == 'Q' || words[i] == 'R' || words[i] == 'S') time += 6;
        else if(words[i] == 'T' || words[i] == 'U' || words[i] == 'V') time += 7;
        else if(words[i] == 'W' || words[i] == 'X' || words[i] == 'Y' || words[i] == 'Z') time += 8;
    }

    cout << time << endl;
}