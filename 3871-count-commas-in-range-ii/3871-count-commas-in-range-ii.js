/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let ans = 0
    let x = 1000
    while (x <= n){
        ans +=  n - x + 1
        x *= 1000
    }
    return ans
};