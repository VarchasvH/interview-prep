# LC 1 - Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Topic: Array / Hashmap
# Difficulty: Easy
# Time taken: <your actual time>

# Intuition: brute force checks every pair (O(n²)).
# Instead, store each number's complement (target - num) in a hashmap.
# If we encounter the complement while iterating, we found our pair.

# Time: O(n) | Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for index, value in enumerate(nums):
            complement = target - value

            if complement in store:
                return [store[complement], index]
           
            store[value] = index
           