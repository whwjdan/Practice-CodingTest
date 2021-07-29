import sys
sys.setrecursionlimit(1000000)

def Tree(nodes):
    n = len(nodes)
    
    if n == 0:
        return []
    root = nodes[0]
    
    for i in nodes:
        if i[1] > root[1]:
            root = i
    c = nodes.index(root)
    
    if c == 0:
        return [root[2], [[], Tree(nodes[1:])]]
    elif c == n - 1:
        return [root[2], [Tree(nodes[:(n - 1)]), []]]
    
    return [root[2], [Tree(nodes[:c]), Tree(nodes[(c + 1):])]]

def preorder(tree):
    if len(tree) == 0:
        return []
    l = [tree[0]]
    l += preorder(tree[1][0])
    l += preorder(tree[1][1])
    return l

def postorder(tree):
    if len(tree) == 0:
        return []
    
    l = postorder(tree[1][0])
    l += postorder(tree[1][1])
    l += [tree[0]]
    return l

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i] = nodeinfo[i] + [i + 1]
    nodeinfo = sorted(nodeinfo, key = lambda k: k[0])
    T = Tree(nodeinfo)
    return [preorder(T), postorder(T)]

#feat(Jeongmu-Jo): [카카오, 2019블라인드] 길찾기게임

