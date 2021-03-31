from btree import tree_define


# 前序便利，根结点-坐节点-右节点
# 递归的方法：时间O(n)，空间O(n)栈的开销
def pre_order1(root):
    result = []

    def traverse(node):
        if node is not None:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result


# 迭代的方法：时间O(n)，空间O(n)栈的开销
def pre_order2(root):
    result = []
    fork = [None]
    while root is not None:
        result.append(root.val)
        if root.left is not None:
            if root.right is not None:
                fork.append(root.right)
            root = root.left
            continue
        elif root.right is not None:
            root = root.right
        else:
            root = fork.pop()

    return result
