"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

# Every string should begin with the prefix!

# If the array is empty, return "". If any string is "", return "".
#
# For index i from 0 to length of the shortest string:
#
# Take the character from the first string at i.
#
# Compare it to all other strings at i.
#
# If mismatch or index out of range, return substring from 0 to i.
#
# If no mismatch, return the shortest string.
#
# Time complexity: O(n * m) where n is number of strings, m is length of the shortest string.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""

        min_length = min(map(len, strs))

        for i in range(min_length):
            char = strs[0][i]

            for el in strs:
                if el[i] != char:
                    return strs[0][:i]
        return strs[0][:min_length]

if __name__ == "__main__":
    sol_instance = Solution()
    print(sol_instance.longestCommonPrefix(strs = ["dog","racecar","car"]))
    print(sol_instance.longestCommonPrefix(strs=["flower","flow","flight"]))








