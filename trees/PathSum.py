from trees import TreeNode


def hasPathSumIter(root: TreeNode, targetSum):
    if not root:
        return False

    stack = [(root, targetSum - root.val), ]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    targetSum -= root.val

    if not root.left and not root.right:
        return targetSum == 0
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
