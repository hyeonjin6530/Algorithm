function solution(price, money, count) {
    let result = 0;
    let all = 0;
    for(let i=1; i<count+1; i++){
        all += price * i;
    }
    
    if(all - money <= 0){
        return 0;
    }
    else{
        return (all - money);
    }
}