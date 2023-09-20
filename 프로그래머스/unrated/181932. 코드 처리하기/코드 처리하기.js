function solution(code) {
    let ret = '';
    let mode = 0;
    
    for(let i=0; i<code.length; i++){
        if(code[i] == "1"){
            if(mode == 0){
                mode = 1;
            }
            else{
                mode = 0;
            }
            
        }
        else if(mode == 0){
            if(i % 2 == 0) ret += code[i];
        }
        else if(mode == 1){
            if(i % 2 != 0) ret += code[i];
        }
    }
    if(ret.length == 0) return "EMPTY";
    else return ret;
}