from typing import List

# Problem:
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

def test_solution():
    testCases = [
        { "input":[[1,2,3], [1,2,4]], "output":[[3], [4]] },
        { "input":[[1,2,3], [1,2,3]], "output":[[], []] },
        { "input":[[1,2,3], [4,5,6]], "output":[[1,2,3], [4,5,6]] },
        { "input":[[1,2,2,3,3], [1,2,2,1]], "output":[[3], []] },
        { "input":[[1,2,2,3,3], [1,2,2,1,3]], "output":[[], []] },
    ]
    solution = Solution()
    for t in testCases:
        assert solution.findDifference(t['input'][0], t['input'][1]) == t['output']