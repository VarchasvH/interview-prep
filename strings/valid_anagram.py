# LC 242 - Valid Anagram
# URL: https://leetcode.com/problems/valid-anagram/
# Topic: String / Hashmap
# Difficulty: Easy
# Time taken: 20 mins (with help)

# Intuition: two strings are anagrams if they contain 
# the same characters with the same frequency.
# Count frequency of each character and compare.

# Approach 1: sorted() — O(n log n) time, O(1) space
# Approach 2: two hashmaps — O(n) time, O(n) space, handles any characters  
# Approach 3: counter array — O(n) time, O(1) space, lowercase only
# Best for interview: ask about input constraints first, then decide

# Time: O(n) | Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s = {}
        seen_t = {}

        for i in range(len(s)):
            seen_s[s[i]] = seen_s.get(s[i], 0) + 1
            seen_t[t[i]] = seen_t.get(t[i], 0) + 1

        return seen_s == seen_t