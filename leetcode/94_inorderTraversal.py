def inorder_helper(node):
    if node is None:
        return []
    leftans = inorder_helper(node.left)
    rightans = inorder_helper(node.right)
    return leftans + [node.val] + rightans

class Solution(object):
    def inorderTraversal(self, root):
        return inorder_helper(root)
