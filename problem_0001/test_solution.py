from solution import Solution 

def test_normal_case():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    answer = s.twoSum(nums, target)

    assert sorted(answer) == [0, 1] 


def test_empty():
    s = Solution()

    nums = []
    target = 0

    answer = s.twoSum(nums, target)
    
    print(answer)
