class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def visit(node):
            if node is None:
                return
            print("入る:", node.val)
            visit(node.left)
            print("記録:", node.val)
            result.append(node.val)
            visit(node.right)
            print("出る:", node.val)

        visit(root)
        return result


def build(values):
    """LeetCodeの配列表記([1,null,2,3])からツリーを作る"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


for values in ([1, None, 2, 3],
               [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]):
    print("=" * 40)
    print("input:", values)
    print("-" * 40)
    print("output:", Solution().inorderTraversal(build(values)))
    print()