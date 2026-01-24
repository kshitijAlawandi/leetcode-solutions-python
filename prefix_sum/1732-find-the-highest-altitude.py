class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sums = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            sums[i + 1] = sums[i] + gain[i]
        return max(sums)

