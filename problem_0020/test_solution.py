from solution import Solution 

def test_true():
    s = Solution()

    assert(s.isValid("()")) == True
    assert(s.isValid("()[]{}")) == True
    assert(s.isValid("{[]}")) == True

def test_false():
    s = Solution()
    assert(s.isValid("([)]")) == False
