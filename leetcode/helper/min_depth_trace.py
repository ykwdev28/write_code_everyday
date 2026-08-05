import sys
import json


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root, depth=0):
        pad = "  " * depth
        print(pad + "担当: " + str(root.val if root else None))

        if root is None:
            print(pad + "-> 0 を返す")
            return 0
        if root.left is None:
            r = self.minDepth(root.right, depth + 1) + 1
            print(pad + "-> 左なし。右の結果+1 = " + str(r))
            return r
        if root.right is None:
            r = self.minDepth(root.left, depth + 1) + 1
            print(pad + "-> 右なし。左の結果+1 = " + str(r))
            return r
        left = self.minDepth(root.left, depth + 1)
        right = self.minDepth(root.right, depth + 1)
        r = min(left, right) + 1
        print(pad + "-> 両方あり。min(" + str(left) + "," + str(right) + ")+1 = " + str(r))
        return r


def build(values):
    """LeetCodeの配列表記からツリーを作る"""
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 min_depth_trace.py '[3,9,20,null,null,15,7]'")
        sys.exit(1)

    values = json.loads(sys.argv[1])  # null -> None に変換される
    print("input:", sys.argv[1])
    print("-" * 40)
    answer = Solution().minDepth(build(values))
    print("-" * 40)
    print("output:", answer)