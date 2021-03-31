from btree import tree_define


# 后序遍历， 左 - 右 - 根
# 递归 O(n) O(n)
def post_order(root):
    result = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
    traverse(root)
    return result


# 迭代
def post_order2(root):
    if not root:
        return list()

    res = list()
    stack = list()
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right

    return res
