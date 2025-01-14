# Sort binary tree by levels
# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []
    
    values = tree_by_level(node, 0, [[node.value]])
    res = [v for value in values for v in value]
    return res

def tree_by_level(node, depth, values):
    if len(values) <= depth:
        values.append([])
    if node.left is not None:
        values[depth].append(node.left.value)
    if node.right is not None:
        values[depth].append(node.right.value)
    if node.left is not None:
        values = tree_by_level(node.left, depth+1, values)
    if node.right is not None:
        values = tree_by_level(node.right, depth+1, values)
    return values
