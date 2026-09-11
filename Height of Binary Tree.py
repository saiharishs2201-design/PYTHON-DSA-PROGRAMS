def tree_height(root):
    if root is None:
        return -1  # use 0 if counting height in "number of nodes" style
    return 1 + max(tree_height(root.left), tree_height(root.right))

# Iterative (BFS) version — height = number of levels - 1
def tree_height_iterative(root):
    if not root:
        return -1
    
    queue = deque([root])
    height = -1
    
    while queue:
        height += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return height

print(tree_height(root))  # 2