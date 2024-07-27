# Problem: 394. Decode String
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are
# well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits
# are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def main(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "]":
                tmpStr = ""
                while stack[-1] != "[":
                    tmpStr = stack.pop() + tmpStr
                stack.pop()
                tmpNum = ""
                while stack and stack[-1].isdigit():
                    tmpNum = stack.pop() + tmpNum
                stack.append(int(tmpNum) * tmpStr)
            else:
                stack.append(i)

        return "".join(stack)


def test_solution():
    testCases = [
        {"input": ["3[a]2[bc]"], "output": "aaabcbc"},
        {"input": ["3[a2[c]]"], "output": "accaccacc"},
        {"input": ["2[abc]3[cd]ef"], "output": "abcabccdcdcdef"},
        {"input": ["abc3[cd]xyz"], "output": "abccdcdcdxyz"},
        {"input": ["10[leetcode]"], "output": "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"},
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
