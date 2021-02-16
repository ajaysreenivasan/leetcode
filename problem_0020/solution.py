class Solution:
    def isValid(self, s:str) -> bool:
        open_set = ['(', '{', '[']
        close_set = [')', '}', ']']

        char_stack = []

        for char in s:
            # Case 1: There's a close parenthesis without a matching open seen.
            if char in close_set and not char_stack:
                return False

            # Case 2: Mismatched open/close parentheses.
            if char in open_set:
                char_stack.append(char)
            elif char in close_set:
                if char == ')' and char_stack[-1] == '(':
                    char_stack.pop()
                elif char == ']' and char_stack[-1] == '[':
                    char_stack.pop()
                elif char == '}' and char_stack[-1] == '{':
                    char_stack.pop()
                else:
                    return False

        # Case 3: There are leftover parentheses without a partner.
        if char_stack:
            return False

        return True
            

def main():
    # THIS METHOD INTENTIONALLY LEFT EMPTY
    pass

main()
