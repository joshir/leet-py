from trees import TreeNode


def postOrderIter(root: TreeNode):
    stack, res = [], []
    while stack or root:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        node = stack.pop()
        if stack and stack[-1] is node.right:
            root = stack.pop()
            stack.append(node)
        else:
            res.append(node.val)
    return res
