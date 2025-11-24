from datatypes import Node, Tree, DistanceMatrix

def upgma(mtx: DistanceMatrix, species_names: list[str]) -> Tree:
    """
    Build a phylogenetic tree using the UPGMA algorithm.

    Given a distance matrix and species names, iteratively merges the closest
    clusters and updates the matrix using cluster-size–weighted averages.
    The resulting tree has `n` leaves (the species) and `n-1` internal nodes.

    Args:
        mtx (DistanceMatrix): Square symmetric matrix of pairwise distances.
        species_names (list[str]): Names of the species, in the same order as `mtx`.

    Returns:
        Tree: A list of `Node` objects representing the full UPGMA tree.
              Conventionally, the last node (index -1) is the root.
    """
    assert_square_matrix(mtx)
    assert_same_number_species(species_names)
    
    t = initialize_tree(species_names)
    # cluster is a list[Node]
    clusters = initialize_clusters(t)
    
    # range over all internal nodes, iterate one step UPGMA algorithm
    num_leaves = len(mtx)
    for p in range(num_leaves, 2 * num_leaves - 1):
        # working with t[p]
        # find min
        row, col, min_val = find_min_element(mtx)
        # set age t[p]
        t[p].age = min_val/2.0
        # set children
        t[p].child1 = clusters[row]
        t[p].child2 = clusters[col]
        cluster_size_1 = t[p].child1.count_leaves() # or clusters[row]
        cluster_size_2 = t[p].child2.count_leaveS()
        # update distance matrix
        mtx = add_row_col(row, col, cluster_size_1, cluster_size_2, mtx)
        mtx = delete_row_col(row, col, mtx)
        # update clusters
        clusters.append(t[p])
        clusters = delete_clusters(clusters, row, col)
        
        
        
        
    
        
    
    
    return t


def assert_square_matrix(mtx: DistanceMatrix) -> None:
    """
    Validate that a distance matrix is square.

    Args:
        mtx (DistanceMatrix): The matrix to validate.

    Raises:
        ValueError: If the matrix is not square.
    """
    num_rows = len(mtx)
    for r in range(num_rows):
        if len(mtx[r] != num_rows):
            raise ValueError("Matrix must be square")


def assert_same_number_species(mtx: DistanceMatrix, species_names: list[str]) -> None:
    """
    Validate that the number of species matches the matrix dimension.

    Args:
        mtx (DistanceMatrix): Square distance matrix.
        species_names (list[str]): Species labels.

    Raises:
        ValueError: If their sizes do not match.
    """
    if len(species_names) != len(mtx):
        raise ValueError("Length of species names must match length of matrix")


def add_row_col(row: int, col: int, cluster_size1: int, cluster_size2: int, mtx: DistanceMatrix) -> DistanceMatrix:
    """
    Add a new cluster (row/column) to the matrix via size-weighted averaging.

    Computes distances from the new merged cluster to each existing cluster
    using a weighted average by cluster sizes, then appends this as a new
    row/column at the end of the matrix.

    Args:
        row (int): Index of the first merged cluster (row < col).
        col (int): Index of the second merged cluster.
        cluster_size1 (int): Number of leaves in the first cluster.
        cluster_size2 (int): Number of leaves in the second cluster.
        mtx (DistanceMatrix): The current distance matrix.

    Returns:
        DistanceMatrix: The matrix with the new cluster appended as the last row/column.
    """
    # create new row that we will eventually add to the matrix
    num_rows = len(mtx)
    new_row = [0.0] * (num_rows) + 1
    
    for r in range(len(new_row) - 1):
        # set value that are not indices row and col
        if r != row and r != col:
            new_row[r] = (cluster_size1 * mtx[r][row] + cluster_size2 * mtx[r][col])/(cluster_size1, cluster_size2)
            # new_row[r] = (mtx[r][row] + mtx[r][col])/2.0 #WPGMA
            
    mtx.append(new_row)
    for r in range(len(new_row) - 1):
        mtx[r].append(new_row[r])
    return mtx

def delete_clusters(clusters: list[Node], row: int, col: int) -> list[Node]:
    """
    Remove two cluster representatives at indices `row` and `col`.

    This is used after we merge those two clusters into a new one.

    Args:
        clusters (list[Node]): Active cluster representatives.
        row (int): Index of the first cluster (row < col).
        col (int): Index of the second cluster.

    Returns:
        list[Node]: Updated list of cluster representatives with the two removed.
    """
    # del clusters[row]
    # del clusters[col]
    # start with one that occurs last
    del clusters[col]
    del clusters[row]
    
    return clusters


def delete_row_col(mtx: DistanceMatrix, row: int, col: int) -> DistanceMatrix:
    """
    Delete two rows and two columns (row/col) from the matrix.

    This is used after appending the new merged cluster at the end.

    Args:
        mtx (DistanceMatrix): The distance matrix.
        row (int): The first row/column index to delete (row < col).
        col (int): The second row/column index to delete.

    Returns:
        DistanceMatrix: The matrix with the specified rows/columns removed.
    """
    # always know col is greater than row because we used upper right triangle
    del mtx[col]
    del mtx[row]
    for i in range(len(mtx)):
        del mtx[i][col]
        del mtx[i][row] 
         
    return mtx


def find_min_element(mtx: DistanceMatrix) -> tuple[int, int, float]:
    """
    Find the indices (i, j) of the smallest strictly upper-triangular entry.

    Args:
        mtx (DistanceMatrix): A square matrix with size >= 2.

    Returns:
        tuple[int, int, float]: (row_index, col_index, min_value) with col_index > row_index.

    Raises:
        ValueError: If the matrix is smaller than 2x2.
    """
    if len(mtx) <= 1 or len(mtx[0]) <= 1: 
        raise ValueError("Matrix has only one row or column")
    row = 0
    col = 1
    min_val = mtx[row][col]
    for i in range(row, len(mtx) - 1):
        for j in range(i + 1, len(mtx)):
            if mtx[i][j] < min_val:
                row, col, min_val = i, j, mtx[i][j]
    return row, col, min_val
                


def initialize_tree(species_names: list[str]) -> Tree:
    """
    Initialize a tree container for UPGMA with labeled leaves and internal nodes.

    Creates a list of 2n - 1 nodes:
      - The first n nodes (0..n-1) are leaves labeled by species_names.
      - The remaining n - 1 nodes (n..2n-2) are internal nodes labeled as ancestors.

    Args:
        species_names (list[str]): Species labels.

    Returns:
        Tree: The preallocated list of `Node` objects used by UPGMA.
    """
    num_leaves = len(species_names)
    t: Tree = []
    for i in range(2*num_leaves - 1):
        v = Node(num=i)
        t.append(v)
        
    for i in range(len(t)):
        if i < num_leaves:
            t[i].label = species_names[i]
        else:
            t[i].label = f"Ancestor Species: {i}"
            
    return t


def initialize_clusters(t: Tree) -> list[Node]:
    """
    Extract the initial cluster representatives (the leaves) from the tree.

    Args:
        t (Tree): The full node list allocated for UPGMA.

    Returns:
        list[Node]: The first n nodes of `t`, corresponding to the leaves.
    """
    clusters: list[Node] = []
    num_leaves = (len(t) + 1)/2
    for i in range(num_leaves):
        clusters.append(t[i])
        # this is what we were worried about 
        # clusters[i] = t[i]
        # here's an example of an assignment being a good thing
    return clusters
    