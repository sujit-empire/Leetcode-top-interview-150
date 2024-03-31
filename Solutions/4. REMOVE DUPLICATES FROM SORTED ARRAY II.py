"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_nums = sorted(nums)
        out_num = []
        for i in range(0, len(new_nums)):
            if new_nums[i] not in out_num:
                out_num.append(new_nums[i])
                if new_nums.count(new_nums[i]) >= 2:
                    out_num.append(new_nums[i])
        print(f"{len(out_num)}, nums = {out_num}")



check = Solution()
check.removeDuplicates([0,2,2,9,9,9,6,6,6,6,5,8])