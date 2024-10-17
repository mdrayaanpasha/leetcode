class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

# Example 1
nums1 = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

# Example 2
nums2 = [2, 0, 1]
Solution().sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]
