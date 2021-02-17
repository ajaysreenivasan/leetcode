from typing import List

class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        seen = []

        def traverse(root):
            if not root:
                return False

            if  target - root.val in seen:
                return True
            else:
                seen.append(root.val)
                return traverse(root.left) or traverse(root.right)

        return traverse(root)


def main():
    # THIS METHOD INTENTIONALLY LEFT EMPTY
    pass

main()
