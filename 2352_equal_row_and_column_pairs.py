from typing import List

# Problem: Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and
# column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        gridReverse = []
        for i in range(n):
            gridReverse.append([grid[j][i] for j in range(n)])
        for i in range(n):
            for j in range(n):
                if grid[i] == gridReverse[j]:
                    count += 1
        return count


def test_solution():
    testCases = [
        {"input": [[[2, 2, 1],
                    [1, 1, 1],
                    [1, 1, 1]]],
         "output": 2},
        {"input": [[[1, 2, 3],
                    [2, 1, 4],
                    [3, 4, 1]]],
         "output": 3},
        {"input": [[[1, 1, 2],
                    [5, 1, 1],
                    [3, 1, 1]]],
         "output": 0},
        {"input": [[[3, 1, 2, 2],
                    [1, 4, 4, 5],
                    [2, 4, 2, 2],
                    [2, 4, 2, 2]]],
         "output": 3},
    ]
    solution = Solution()
    correct = 0
    print("Testing solution...")
    for t in testCases:
        result = True
        if solution.equalPairs(*t['input']) == t['output']:
            print(f"Passed Test Case {t['input']}")
            correct += 1
        else:
            print(
                f"Failed Test Case {t['input']} expected {t['output']} actual {solution.equalPairs(*t['input'])}")
            result = False
    print(f"Passed {correct} out of {len(testCases)} test cases")
    assert result
