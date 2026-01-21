class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sums = [0] * (len(self.nums) + 1)

        for i in range(len(self.nums)):
            sums[i + 1] = sums[i] + self.nums[i]

        return sums[right + 1] - sums[left]
