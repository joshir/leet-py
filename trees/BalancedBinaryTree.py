from trees import TreeNode


class Solution:
    def __init__(self):
        self.res = None

    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True

        def dfs(node):
            if node is None:
                return -1
            l_height, r_height = dfs(node.left), dfs(node.right)
            if abs(l_height - r_height) > 1:
                self.res = False

            return max(l_height, r_height) + 1

        dfs(root)
        return self.res
