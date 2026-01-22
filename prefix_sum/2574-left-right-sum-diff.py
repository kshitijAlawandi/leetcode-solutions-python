class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sums = [0] * len(nums)
        right_sums = [0] * len(nums)
        running_total = 0
        final_list = []

        for i in range(len(nums) - 1):
            left_sums[i + 1] = left_sums[i] + nums[i]
        for j in range(len(nums) - 1, -1, -1):
            right_sums[j] = running_total
            running_total += nums[j]
        for i in range(len(nums)):
            final_list.append(abs(left_sums[i] - right_sums[i]))

        return final_list
