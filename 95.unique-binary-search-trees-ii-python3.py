# @leet start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val=val)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = TreeNode(val=val)
            else:
                self.right.add(val)


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        options = list(range(1, n + 1))

        def generate(options):
            # print(options)
            if len(options) == 0:
                return [None]
            if len(options) == 1:
                return [TreeNode(val=options[0])]
            trees = []
            for i in range(len(options)):
                left = generate(options[:i])
                right = generate(options[i + 1 :])
                for l in left:
                    for r in right:
                        root = TreeNode(val=options[i])
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return generate(options)


# @leet end
