"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19

Output: true

Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:

Input: n = 2
Output: false

Constraints:

1 <= n <= 231 - 1

187
1 + 64 + 49 = 114
1 + 1 + 16 = 18
1 + 64 = 65
36 + 25 = 61
36 + 1 = 37
9 + 49 = 58
25 + 64 = 89 <---
64 + 81 = 145
1 + 16 + 25 = 42
16 + 4 = 20
4 + 0 = 4
4**2 = 8
8**2 = 64
36 + 16 = 52
25 + 4 = 29
4 + 81 = 85
64 + 25 = 89 <---
64 + 81 = 145
1 + 16 + 25 = 42
16 + 4 = 20
4 + 0 = 4


11
1 + 1 = 2
4
8
16
1 + 36 = 37
...

17
1 + 49 = 50
25 + 0 = 25
4 + 25 = 29
4 + 81 = 85
64 + 25 = 89 <---
64 + 81 = 145
1 + 16 + 25 = 42
16 + 4 = 20
4 + 0 = 4
4**2 = 16
...
25 + 64 = 89 <---

3 - 9 - 81 - (9) - 81
4 - 16 - 37 - 58 - 89 - 145 - 42 - 20 - (4)
5 - 25 - 29 - 85- 89 - 145 ... (89)
6 - 36 - 45 - 41 - 17 - 50 - 25 - 29 - 85 - 89 - ... - (89)
7 - 49 - 97 - 130 - 10 - 1 == BINGO == True
8 - 64 - 52 - 29 - 85 - 89 - 145 - 42 - 20 - 4 - (8)
9 - 81 - (9)
10 = 1 == BINGO == True
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        sum_list = set()

        while True:
            sum_result = sum([d**2 for d in map(int, str(n))])

            if sum_result == 1:
                return True
            elif sum_result in sum_list:
                break

            sum_list.add(sum_result)
            n = sum_result

        return False


if __name__ == "__main__":
    sol_instance = Solution()
    print(sol_instance.isHappy(int(input())))


