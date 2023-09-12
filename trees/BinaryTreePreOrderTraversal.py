from trees import TreeNode


def preOrderTraversal(root: TreeNode):
    res = []

    def dfs(root):
        if root is None:
            return
        else:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

    return res


def preOrderIter(root: TreeNode):
    cur, stack, res = root, [], []
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res
