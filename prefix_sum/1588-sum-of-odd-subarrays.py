class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        final_sums = []
        final_output = 0
        sums_list = []
        f1 = []

        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)+1):
        #         sums_list.append(arr[i:j])
        # print(sums_list)
        sums_list = [arr[i:j] for i in range(len(arr)) for j in range(i+1,len(arr)+1)]

        for j in sums_list:
            if len(j)%2 != 0:
                final_sums.append(j)
        # print(final_sums)

        for k in final_sums:
            f1.append(sum(k))
        return sum(f1)
