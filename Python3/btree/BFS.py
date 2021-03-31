from btree.tree_define import Btree


def BFS(root):
    if not root:
        return []

    res = [[]]

    def bfs(node, level):
        if node is None:
            return
        try:
            res[level].append(node.val)
        except IndexError:
            res.append([node.val])
        bfs(node.left, level+1)
        bfs(node.right, level+1)
    bfs(root, 0)
    return res

