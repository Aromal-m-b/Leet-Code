class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while 0 in nums:
            count+=1
            nums.remove(0)
        nums.extend([0]*count)