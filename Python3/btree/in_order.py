from btree import tree_define


# 中序遍历，左节点 - 根节点 - 右节点
# 递归 时间O(n) 空间O(n)
def in_order(root):
    result = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result


# 迭代 O(n) O(n)
def in_order2(root):
    result = []
    stack = []
    while stack or root is not None:
        if root is None:
            root = stack.pop()
            result.append(root.val)
            root = root.right
            continue
        while root.left is not None:
            stack.append(root)
            root = root.left
        result.append(root.val)
        root = root.right

    return result

