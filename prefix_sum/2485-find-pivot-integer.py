class Solution:
    def pivotInteger(self, n: int) -> int:
        og_list = [i + 1 for i in range(n)]
        sums_left = [0] * n
        sums_right = [0] * n
        right_run_total = 0
        final_out = 0

        for i in range(n):
            sums_left[i] = sums_left[i - 1] + og_list[i]

        for j in range(n - 1, -1, -1):
            sums_right[j] = right_run_total + og_list[j]
            right_run_total += og_list[j]

        for i in range(len(og_list)):
            if sums_left[i] == sums_right[i]:
                final_out = og_list[i]
                break
            else:
                final_out = -1
        return final_out

