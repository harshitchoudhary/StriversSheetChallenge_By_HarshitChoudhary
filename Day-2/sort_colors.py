class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums)-1
        i = 0

        while i <= right:
            if nums[i] == 0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
            elif nums[i] == 2:
                temp1 = nums[right]
                nums[right] = nums[i]
                nums[i] = temp1
                right -= 1
                i-= 1
            i += 1