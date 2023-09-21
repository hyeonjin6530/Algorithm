function solution(myString) {
    let answer = '';
    
    for(let i=0; i<myString.length; i++){
        if(myString[i] == "a"){
            answer += "A";
        }
        else if(myString[i] != "A"){
            answer += myString[i].toLowerCase();
        }
        else{
            answer += "A"
        }
    }
    
    return answer;
}