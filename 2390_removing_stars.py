from typing import List

# Problem:
# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
#
# Note:
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


class Solution:
    def main(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


def test_solution():
    testCases = [
        {"input": ["leet**cod*e"], "output": "lecoe"},
        {"input": ["erase*****"], "output": ""},
    ]
    solution = Solution()
    correct = 0
    print("Testing solution...")
    for t in testCases:
        result = True
        if solution.main(*t['input']) == t['output']:
            print(f"Passed Test Case {t['input']}")
            correct += 1
        else:
            print(
                f"Failed Test Case {t['input']} expected {t['output']} actual {solution.main(*t['input'])}")
            result = False
    print(f"Passed {correct} out of {len(testCases)} test cases")
    assert result
