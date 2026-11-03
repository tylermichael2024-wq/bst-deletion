# Binary Search Tree Deletion

A binary search tree (BST) in Python with full support for deleting values. Deletion handles all three cases, including removing the root, and the tree stays correctly ordered with an accurate size count after every removal.

Built for my Data Structures & Algorithms coursework at the University of Mount Olive.

## Files

| File | What it contains |
|---|---|
| `container.py` | The node class. Each node stores a value and links to a smaller (`lt`) and a greater (`gt`) child. |
| `tree.py` | The BST: insert (`append`), search (`contains`), depth-first traversal (`dfs_traverse`), and deletion (`delete`). |
| `test.py` | Builds a sample tree and tests searching, traversal and every deletion case. |

## How deletion works

`delete(value)` searches recursively for the value. Each step returns the new root of the subtree it came from, so every parent's link is reattached correctly after a removal. Once the value is found, there are three cases:

1. **Leaf (no children):** the node is removed.
2. **One child:** the node is replaced by its only child.
3. **Two children:** the node takes the value of its in-order successor (the smallest value in its right subtree), and that successor is then removed from the right subtree.

If the value isn't in the tree, an error message is printed and the tree is left unchanged.

## Running it

Requires Python 3.

```bash
python test.py
```

Expected output:

```
7
True
False
Checked 15
Checked 1
Checked 9
Checked 17
Checked 31
Checked 24
Checked 65
ERR: 100 is not stored in the tree.
3
False
```

The test builds a tree from 15, 17, 31, 1, 9, 24 and 65, then deletes a value that isn't stored (100), two leaves (65 and 24), a node with one child (17) and the root with two children (15). Three values remain afterward.

## Tech

Python · Recursion · Binary search trees
