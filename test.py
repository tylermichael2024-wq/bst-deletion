from tree import tree
from container import container

my_tree = tree( )

my_tree.append(15)
my_tree.append(17)
my_tree.append(31)
my_tree.append(1)
my_tree.append(9)
my_tree.append(24)
my_tree.append(65)

print(my_tree.size)

print(my_tree.contains(9))
print(my_tree.contains(55))

my_tree.dfs_traverse(my_tree.root)

#delete tests
my_tree.delete(100)   #not in tree. should be error message
my_tree.delete(65)    #leaf
my_tree.delete(24)    #leaf
my_tree.delete(17)    #one child
my_tree.delete(15)    #root, two children
print(my_tree.size)   #should be 3
print(my_tree.contains(15))  #false
