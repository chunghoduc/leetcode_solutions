from typing import List

# Problem 735. Asteroid Collision:
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
#
#
# Example 1:
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
#
# Constraints:
#
# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

class Solution:
    def main(self, asteroids: List[int]) -> List:
        stack = []
        for i in range(len(asteroids)):
            if len(stack) == 0:
                stack.append(asteroids[i])
            else:
                if asteroids[i] < 0:
                    while len(stack) > 0 and 0 < stack[-1] < abs(asteroids[i]):
                        stack.pop()
                    if len(stack) == 0:
                        stack.append(asteroids[i])
                        continue
                    if stack[-1] + asteroids[i] == 0:
                        stack.pop()
                    elif stack[-1] > abs(asteroids[i]):
                        continue
                    else:
                        stack.append(asteroids[i])
                elif asteroids[i] > 0:
                    stack.append(asteroids[i])
        return stack


def test_solution():
    testCases = [
        {"input": [[5, 10, -5]], "output": [5, 10]},
        {"input": [[5, 10, -5, -5]], "output": [5, 10]},
        {"input": [[5, 10, -10, -5]], "output": []},
        {"input": [[5, 10, -5, -10]], "output": [5]},
        {"input": [[5, 10, 2, -5]], "output": [5, 10]},
        {"input": [[5, 10, -5, 2, -10, -10]], "output": [-10]},
        {"input": [[-5, -10, -5, 2, 3, 4]], "output": [-5, -10, -5, 2, 3, 4]},
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
