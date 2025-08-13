from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0  # Position to place the next non-zero element

        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Step 2: Fill the remaining positions with 0
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
nums = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
