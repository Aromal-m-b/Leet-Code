class Solution {
    public String removeOuterParentheses(String s) {
        String res = "";
        int count = 0;
        int start = 0;
        for(int i  = 0;i<s.length();i++){
            if(s.charAt(i) == '('){
                count += 1;
            }else{
                count -= 1;
            }
            if(count == 0){
                res = res + s.substring(start+1,i);
                start = i+1;
            }
        }
        return res;
    }
}