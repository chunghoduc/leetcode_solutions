# Problem: 1657. Determine if Two Strings Are Close
# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        word1_count = [word1.count(c) for c in set(word1)]
        word2_count = [word2.count(c) for c in set(word2)]
        # print(sorted(word1_count), sorted(word2_count))
        return sorted(word1_count) == sorted(word2_count)


def test_solution():
    testCases = [
        { "input": ["abc", "bca"], "output": True },
        { "input": ["a", "aa"], "output": False },
        { "input": ["cabbba", "abbccc"], "output": True },
        { "input": ["cabbba", "aabbss"], "output": False },
        { "input": ["cabbba", "aabbcc"], "output": False },
    ]
    solution = Solution()
    for t in testCases:
        result = True
        if solution.closeStrings(t['input'][0], t['input'][1]) == t['output']:
            print(f"Passed Test Case {t['input']}")
        else:
            print(f"Failed Test Case {t['input']} expected {t['output']} actual {solution.closeStrings(t['input'][0], t['input'][1])}")
            result = False
    assert result

