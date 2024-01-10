# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Two binary trees are considered leaf-similar if their leaf value sequence is the same.

        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
        """
        def get_leaf_sequence(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return get_leaf_sequence(root.left) + get_leaf_sequence(root.right)
        return get_leaf_sequence(root1) == get_leaf_sequence(root2)