from solution import Solution 

def test_normal_case():
    s = Solution()

    root = [5, 3, 6, 2, 4, None, 7]
    k = 9

    assert s.FindTarget == True


def test_empty():
