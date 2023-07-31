from Python3.btree.tree_define import Btree


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
res = []
def dfs(root):


    if not root:
        return
    res.append(root.val)
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)
    return res


root = Btree(1, Btree(2, Btree(4, None, None), None), Btree(3, Btree(5, Btree(7, None, None), None), Btree(6, None, None)))
print(dfs(root))