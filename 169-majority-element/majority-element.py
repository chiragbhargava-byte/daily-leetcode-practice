class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0 
        n = len(nums)

        for num in nums :
            if count == 0 :
                element = num
                count = 1
            elif num == element:
                count += 1
            else :
                count -= 1

        cnt2 = nums.count(element) 
        if cnt2 > n//2 :
            return element

        return -1
        