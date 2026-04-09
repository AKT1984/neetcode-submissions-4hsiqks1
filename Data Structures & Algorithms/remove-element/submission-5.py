class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return int(val != nums[0])

        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] != val:
                left += 1

            while left < right and nums[right] == val:
                right -= 1

            if left < right:
                nums[left] = nums[right]
                right -= 1

        return left + int(nums[left] != val)        
