class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        hmap = {}

        def solve(i):

            # memoization
            if i in hmap:
                return hmap[i]

            # minimum path length is the node itself
            best = 1

            # explore left
            for j in range(i - 1, max(i - d - 1, -1), -1):

                # blocking condition
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + solve(j))

            # explore right
            for j in range(i + 1, min(i + d + 1, len(arr))):

                # blocking condition
                if arr[j] >= arr[i]:
                    break

                best = max(best, 1 + solve(j))

            hmap[i] = best
            return best

        result = 1

        for i in range(len(arr)):
            result = max(result, solve(i))

        return result