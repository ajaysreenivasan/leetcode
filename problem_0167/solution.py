from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        temp = nums[i] + nums[j]

        while(temp != target):
            temp = nums[i] + nums[j]

            if(temp < target):
                i += 1
            elif(temp > target):
                j -= 1

        return [i+1, j+1]

def main():
    # THIS METHOD INTENTIONALLY LEFT EMPTY
    pass

main()
