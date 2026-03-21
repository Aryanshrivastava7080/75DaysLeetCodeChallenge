class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lft = 0

        for rght in range(len(nums)):
            if nums[rght] != 0:
                nums[rght], nums[lft] = nums[lft], nums[rght]
                lft += 1
        
        return nums
           

        