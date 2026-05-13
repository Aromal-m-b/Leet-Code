class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2*limit+2)
        for i in range (0,n//2):
            a = nums[i]
            b = nums[n-i-1]

            #initialize the diff list case 3 , we need 2 moves
            diff[2] += 2
            diff[2*limit+1] -= 2

            #case 2 we need only one move
            low = min(a,b) + 1
            high = max(a,b) + limit

            diff[low] -= 1
            diff[high+1] += 1

            diff[a+b] -= 1
            diff[a+b+1] += 1

        ans = float(inf)
        mov = 0
        print(diff)
        for i in range(2,2*limit+1):
            mov += diff[i]
            ans = min(ans,mov)
        return ans
