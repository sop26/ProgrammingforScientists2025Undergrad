from functions import upgma
from io_util import read_matrix_from_file, write_newick_to_file
from datatypes import Node


def main() -> None:
    print("Happy trees.")
    
    filename = "Data/HBA1/hemoglobin.mtx"
    
    species_names, mtx = read_matrix_from_file(filename)
    
    t = upgma(mtx, species_names)
    
    write_newick_to_file(t, "Output/HBA1", "hba1.tre")
    
    
    filename = "Data/UK-SARS-CoV-2/SARS_spike.mtx"
    
    species_names, mtx = read_matrix_from_file(filename)
    
    t = upgma(mtx, species_names)
    
    write_newick_to_file(t, "Output/UK-SARS-CoV-2", "sars-cov-2.tre")
    
    
    # write tree to file so we can visualize it
    # classic example everyone needs to agree on how we write tree to file
    