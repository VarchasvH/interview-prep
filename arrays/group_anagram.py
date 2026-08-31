# LC 49 - Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/
# Topic: Array / Hashmap
# Difficulty: Medium
# Time taken: 12 mins (looked at solution)

# Intuition: two words are anagrams if they have identical character frequencies.
# Use the frequency signature as a hashmap key to group anagrams together.
# tuple() needed because lists are mutable and can't be dictionary keys.

# Approach 1: sorted string as key — O(n·k·log k) time, simpler to think of
# Approach 2: count array as key — O(n·k) time, optimal
# Best for interview: start with Approach 1, mention Approach 2 as optimization

# Time: O(n·k) | Space: O(n·k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            seen[tuple(count)].append(s)

        return list(seen.values())