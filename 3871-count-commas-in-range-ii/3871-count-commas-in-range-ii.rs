impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut ans : i64 = 0;
        let mut x : i64 = 1000;
        while x<=n {
            ans =  ans + (n - x + 1);
            x = x * 1000;
        }
        ans
    }
}