class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)):
            if nums[ans]!=nums[i]:
                ans+=1
                nums[ans]=nums[i]
        return ans+1
