class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        
        best_single_value = max_val - min_val
        
        return k * best_single_value