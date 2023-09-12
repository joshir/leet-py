from trees import TreeNode


def dfs(left: TreeNode, right: TreeNode) -> bool:
    if not left and not right:
        return True
    if not left or not right:
        return False

    return left.val == right.val and dfs(left.left, right.right) and dfs(left.right,right.left)


def isSymmetric(root: TreeNode) -> bool:
    if not root: return True
    return dfs(root.left, root.right)