from collections import deque

from trees import TreeNode


def maxDepth(root: TreeNode):
    if not root:
        return 0
    else:
        return 1 + (maxDepth(root.left), maxDepth(root.right))


def maxDepthIterative(root: TreeNode):
    if not root:
        return 0
    q = deque()
    q.append(root)
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def maxDepthIterativeDFS(root: TreeNode):
    stack = [(root, 1)]
    depth = 0
    while stack:
        node, cur_depth = stack.pop()
        if node:
            depth = max(depth, cur_depth)
            stack.append((node.left, cur_depth + 1))
            stack.append((node.right, cur_depth + 1))
    return depth
