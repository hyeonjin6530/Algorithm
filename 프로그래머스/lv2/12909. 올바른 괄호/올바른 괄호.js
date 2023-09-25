function solution(s){
    let answer = true;
    const a = s.split("");
    let count = 0;
    
    a.forEach(item => {
        item == "(" ? count++ : count--;
        if (count < 0) answer = false;
    } );
    
    if(count != 0) answer = false;
    return answer;
}