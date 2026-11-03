# The container object will contain a single integer
# and a "pointer" to the next container in the linked list

class container( ):
    # Define the initialization method
    def __init__(self,v):
        # Initialize the values of two attributes
        # self.value is the integer that we want to store in the container
        self.value = v

        # self.gt is a "pointer" to the next container storing a greater value
        self.gt = None
        # self.lt is a "pointer" to the next container storing a lower value
        self.lt = None

        # self.checked is used for DFS
        self.checked = False

    # This function links this container to the container n passed as
    # an argument
    def link_to_gt(self,n): # Link to 'gt' pointer
        self.gt = n
        
    def link_to_lt(self,n): # Link to 'lt' pointer
        self.lt = n

