function solution(s) {
    let answer = '';
    const arr = s.split(" ");
    const a= arr.map(Number);
    let min = a[0];
    let max = a[0];
    
    a.forEach(num => {
        if(num < min) min = num;
        if(num > max) max = num;
    } );
    
    answer = min + " " + max;
    return answer;
}