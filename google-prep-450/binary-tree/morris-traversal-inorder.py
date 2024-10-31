class Solution:
    def inorderMorrisTraversal(self, root):
        result = []

        curr = root 

        while curr:
            if curr.left == None:
                result.append(curr.val)
                curr = curr.right 

            else:
                ## find the right most node of left subtree
                prev = curr.left

                while prev.right and prev.right != curr: ## if there is not already made connection
                    prev = prev.right 
                
                ## case 1 if right is null

                if prev.right == None:
                    prev.right = curr 
                    curr = curr.left

                ## means we have already made the connection
                else:
                    prev.right = None ## remove the connection
                    result.append(curr.val)
                    curr = curr.right 


        return result 
