class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        breaks = 0
        for i in range(1,n) :
            if nums[i] < nums[i - 1] :
                breaks += 1
        
        if nums[-1] > nums[0] :
            breaks += 1

        return breaks <= 1

obj = Solution()
nums = [3,4,5,6]
print(obj.check(nums))

