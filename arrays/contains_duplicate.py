# LC 217 - Contains Duplicate
# URL: https://leetcode.com/problems/contains-duplicate/
# Topic: Array / Hashmap
# Difficulty: Easy
# Time taken: 10 mins

# Intuition: use a set to track numbers seen so far.
# If we encounter a number already in the set, it's a duplicate.
# Set lookup is O(1) so no need to scan the whole array each time.

# Time: O(n) | Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False