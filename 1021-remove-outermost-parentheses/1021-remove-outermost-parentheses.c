char* removeOuterParentheses(char* s) {
    int n = strlen(s);
    char *res = malloc(n+1);
    res[0] = '\0';
    int count= 0;
    int start = 0;
    for(int i = 0;i<strlen(s);i++){
        if(s[i] == '('){
            count++;
        }else{
            count--;
        }
        if(count == 0){
            strncat(res,s+start+1,i-start-1);
            start = i+1;
        }
    }
    return res;
}