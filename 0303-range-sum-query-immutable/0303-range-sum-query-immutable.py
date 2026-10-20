class NumArray:

    def __init__(self, nums: list[int]):
        self.ip = nums
        ir = iter(self.ip)
        self.rt = [next(ir)]
        for val in ir:
            self.rt.append(self.rt[-1] + val)
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.rt[right] - self.rt[left-1]
        else:
            return self.rt[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)