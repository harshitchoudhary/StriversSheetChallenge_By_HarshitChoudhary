class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(nums, startIndex):
            i, j = startIndex, len(nums) - 1

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i + 1)