from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_index = {}
        
        for index, num in enumerate(nums):
            diff = target - num
              
            if num in diff_index.keys():
                if index != diff_index[num]:
                    return [index, diff_index[num]]
            
            diff_index[diff] = index


def main():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    print(s.twoSum(nums, target))


main()
