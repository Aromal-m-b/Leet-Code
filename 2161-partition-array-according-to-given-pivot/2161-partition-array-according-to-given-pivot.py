class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        mid =[]
        for i in range(len(nums)):
            if nums[i] == pivot:
                mid.append(pivot)
            elif nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return left+mid+right