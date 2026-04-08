class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        for item in nums:
            if item == 0:
                count = 0
            else:
                count += 1
            if max < count:
                    max = count
        
        return max
    