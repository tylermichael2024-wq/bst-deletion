# A Python implementation of a Binary Search Tree (BST)
from container import container

class tree( ):
    # Define the initialization method
    def __init__(self):
        self.size = 0
        self.root = None

    def is_empty(self):
        return self.size == 0

    def dfs_traverse(self,c):
        # 1. Initialize an empty stack of nodes
        stack = [ ]

        # 2. Push the node we start DFS from (c) to the stack
        stack.insert(0, c)

        # 3. Begin the search
        while len(stack) > 0:
            # 4. Pop the node at the top of the stack
            c = stack.pop(0)

            if c.checked == False:
                c.checked = True
                print(f"Checked {c.value}")

                # push gt first so lt is on top and gets visited first
                if c.gt != None:
                    stack.insert(0, c.gt)
                if c.lt != None:
                    stack.insert(0, c.lt)
            

    def append(self,v):
        if self.root == None:
            self.root = container(v)
            self.size += 1

            return
        
        current_node = self.root

        while True:
            if current_node.value == v:
                print("ERR: This value is already stored.")
                return

            if v < current_node.value:
                if current_node.lt != None:
                    current_node = current_node.lt
                    continue
                else:
                    current_node.link_to_lt(container(v))
                    self.size += 1

                    return
            elif v > current_node.value:
                if current_node.gt != None:
                    current_node = current_node.gt
                else:
                    current_node.link_to_gt(container(v))
                    self.size += 1

                    return

    def contains(self,v):
        if self.root == None:
            return False

        current_node = self.root

        while True:
            if current_node.value == v:
                return True

            if v < current_node.value:
                if current_node.lt != None:
                    current_node = current_node.lt
                    continue
                else:
                    return False
            elif v > current_node.value:
                if current_node.gt != None:
                    current_node = current_node.gt
                    continue
                else:
                    return False
    



    #start of deletion (assignment)
    #leftmost node, so keep going left until there is no lt child.
    def findBSTmin(self, k):
        while k.lt != None:
            k = k.lt
        return k

    #removes the smallest node in a subtree
    #and returns the (possibly new) root of that subtree.
    def deleteBSTmin(self, k):
        #empty subtree, nothing to delete
        if k == None:
            return None

        #k is the minimum. Removing it means returning its
        # gt child, so whoever pointed at k now points at k.gt instead.
        if k.lt == None:
            temp = k.gt
            return temp

        #otherwise the minimum is further left, so recurse down the lt
        #side and reattach whatever comes back.
        k.lt = self.deleteBSTmin(k.lt)
        return k

    #deletes value from the subtree rooted at k and
    #returns the new root of that subtree.
    def deleteBST(self, k, value):
        if k == None:
            print(f"ERR: {value} is not stored in the tree.")
            return None

        #go left or right, and reattach the result
        #so the parent's pointer stays correct if the child changed.
        if value < k.value:
            k.lt = self.deleteBST(k.lt, value)
            return k
        if value > k.value:
            k.gt = self.deleteBST(k.gt, value)
            return k

        #exactly one container is removed, so update size.
        self.size -= 1

        #replace this node with its only child(or None)
        if k.lt == None:
            return k.gt
        if k.gt == None:
            return k.lt

        temp = self.findBSTmin(k.gt)
        k.value = temp.value
        k.gt = self.deleteBSTmin(k.gt)
        return k


    def delete(self, value):
        self.root = self.deleteBST(self.root, value)
    
