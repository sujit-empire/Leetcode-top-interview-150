"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
#leetcode que 238
# link -> https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
# ref to understand still i didn't understand -> https://youtu.be/5bS636lE_R0

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left_product, right_product = 1, 1

    # Calculate products of elements to the left of each element
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]

    # Calculate products of elements to the right of each element and combine with left product
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Test the function with the given examples
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]