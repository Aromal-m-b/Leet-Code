class Solution {
    public int gcdOfOddEvenSums(int n) {
        int a = n*n;
        int b = n*(n+1);
        int temp;
        if (a < b){
            temp = a;
            a = b;
            b = temp;
        } 
        while(a%b != 0){
            temp = b;
            b = a%b;
            a = b;
        }
        return b;
    }
}