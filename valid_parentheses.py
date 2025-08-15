"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def check_validity(s):
    brackets_stack = []

    pairs = {')': '(', ']': '[', '}': '{'}

    for el in s:
        if el in '{[(':
            brackets_stack.append(el)
        elif len(brackets_stack) > 0 and brackets_stack[-1] == pairs.get(el):
            brackets_stack.pop()
        else:
            return False

    return not brackets_stack

user_input = input()
print(check_validity(user_input))



