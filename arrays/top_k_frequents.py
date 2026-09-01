# LC 347 - Top K Frequent Elements
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Topic: Array / Hashmap / Bucket Sort
# Difficulty: Medium
# Time taken: 30 mins (with help)

# Intuition: count frequency of each number, then find the k most frequent.
# Key insight for bucket sort: frequency can't exceed len(nums),
# so create buckets indexed by frequency and scan from highest down.
# freq[3] = [all numbers that appear 3 times]

# Approach 1: sorted hashmap — O(n log n), simplest
# Approach 2: min heap — O(n log k), classic top-K pattern, good interview answer
# Approach 3: bucket sort — O(n), optimal
# Best for interview: start with heap, mention bucket sort as optimization

# Time: O(n) | Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res