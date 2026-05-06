# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        
        
        nodes = deque()
        if root:
            nodes.append(root)
            res.append(root.val)

        while nodes:
            cur_len = len(nodes)
            for i in range(cur_len):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            if nodes:
                res.append(nodes[-1].val)

        return res



            


        
            
        

        

            
        