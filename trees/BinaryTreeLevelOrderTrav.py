from collections import deque
from typing import List

from trees import TreeNode


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    q, res = deque([root]), []
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
