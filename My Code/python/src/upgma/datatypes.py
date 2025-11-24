from dataclasses import dataclass
from typing import Self

# distance matrix alias, node declaration, tree declaration

DistanceMatrix = list[list[float]]

@dataclass
class Node:
    """
    Represents a node in a phylogenetic tree.
    
    Attributes:
        num (int): numeric ID for the node
        age (float): represents its "age" from the leabes
        label (str): species name for leaves, ancestor name for internal nodes
        child1: the first child node, or None if we're at a leaf
        child2: the second child node or None if we're at a leaf
    """
    num: int = 0
    age: float = 0.0
    label: str = ""
    child1: Self | None = None
    child2: Self | None = None
    
    def is_leaf(self) -> bool:
        """
        Method that returns true if given node is a leaf. False otherwise.
        """
        if self.child1 == None and self.child2 == None:
            return True
        return False
    
    def count_leaves(self) -> int:
        # leaf or internal node
        if self.is_leaf():
            return 1
        leaves = 0
        
        if self.child1 is not None:
            leaves += self.child1.count_leaves()
        if self.child2 is not None:
            leaves += self.child2.count_leaves()
        return leaves
        
    
Tree = list[Node]