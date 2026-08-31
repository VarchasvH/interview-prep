# LC 125 - Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/
# Topic: String / Two Pointer
# Difficulty: Easy
# Time taken: 20 mins (with help)

# Intuition: clean the string to alphanumeric only, then
# use two pointers from both ends moving inward.
# If any mismatch found, not a palindrome.
# Skip non-alphanumeric characters in place instead of cleaning first.

# Approach 1: clean string + reverse — O(n) time, O(n) space
# Approach 2: two pointers in place — O(n) time, O(1) space
# Best for interview: Approach 2

# Time: O(n) | Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True