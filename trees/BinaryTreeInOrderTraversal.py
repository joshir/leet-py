from trees import TreeNode


def inOrderTraversal(root: TreeNode):
    res = []

    def dfs(root):
        if root is None:
            return
        else:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

    return res


def inOrderIter( root: TreeNode):
    res, stack, cur = [], [], root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res
