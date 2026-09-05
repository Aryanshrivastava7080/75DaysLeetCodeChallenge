class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Suffix Minimum Precomputation
        suffMin = [0] * n
        suffMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])
            
        # Prefix Maximum Precomputation + Check on the fly
        currMax = float('-inf')
        for i in range(n):
            currMax = max(currMax, nums[i])
            if currMax - suffMin[i] <= k:
                return i
                
        return -1