
from tree import Tree

def run_tree_tests():
    
    mytree = Tree();
    mytree.add(5, "Peter")
    mytree.add(3, "Paul")
    mytree.add(1, "Mary")
    mytree.add(10, "Karla")
    mytree.add(15, "Ada")
    mytree.add(25, "Kari")
    
    #inorder_nodes = mytree.inorder()
    
    #print(f"inorder_nodes = {inorder_nodes}")
    
    bfs_nodes = mytree.bfs_print()
    
    print(f"bfs_nodes = {bfs_nodes}")
    

run_tree_tests()
    
    