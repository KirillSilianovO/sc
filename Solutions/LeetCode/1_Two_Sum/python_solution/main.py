from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        nums_len = len(nums)
        for i in range(nums_len):
            checked_item = target - nums[i]
            if checked_item in checked:
                return [i, checked[checked_item]]
            checked[nums[i]] = i
        return []


class TestSolution(unittest.TestCase):
    solution: Solution = None

    def setUp(self):
        self.solution = Solution()

    def test_two_sum_1(self):
        num = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(sorted(self.solution.twoSum(num, target)), sorted(expected))

    def test_two_sum_2(self):
        num = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(sorted(self.solution.twoSum(num, target)), sorted(expected))

    def test_two_sum_3(self):
        num = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(sorted(self.solution.twoSum(num, target)), sorted(expected))


if __name__ == '__main__':
    unittest.main()
