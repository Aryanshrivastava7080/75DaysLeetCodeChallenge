class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}

        n = len(nums)

        # Har subarray of size k
        for i in range(n - k + 1):
            seen = set()

            # Current window
            for j in range(i, i + k):
                seen.add(nums[j])

            # Har distinct element ka count
            for x in seen:
                count[x] = count.get(x, 0) + 1

        # Exactly 1 subarray me aane wale elements
        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans