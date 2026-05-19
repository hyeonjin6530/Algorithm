# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 가장 아래까지 내려갔는데 노드가 없을 경우
        if not root:
            return None
        
        # 현재 노드가 p 또는 q인지 확인
        if root == p or root == q:
            return root
        
        # 왼쪽 탐색
        left = self.lowestCommonAncestor(root.left, p, q)

        # 오른쪽 탐색
        right = self.lowestCommonAncestor(root.right, p, q)

        # 둘 다 값이 있다면? -> 현재 노드가 공통 조상이라는 뜻
        if left and right:
            return root

        if left:
            return left
        
        return right
