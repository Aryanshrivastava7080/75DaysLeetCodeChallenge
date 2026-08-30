class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        i = min(min_index, max_index)
        j = max(min_index, max_index)

        case1 = j + 1
        case2 = n - i
        case3 = (i + 1) + (n - j)

        return min(case1, case2, case3)