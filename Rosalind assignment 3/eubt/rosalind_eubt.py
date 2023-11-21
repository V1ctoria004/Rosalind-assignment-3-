from itertools import permutations

def generate_unrooted_trees(species_names):
    n = len(species_names)
    trees = []

    for perm in permutations(species_names):
        tree_str = "(".join(perm) + ")"  # Join the species names in Newick format
        tree_str += species_names[0] + ";"  # Add the root species and semicolon
        trees.append(tree_str)

    return trees

def main():
    # Read input from file
    with open('rosalind_eubt.txt', 'r') as file:
        species_names = file.readline().strip().split()

    # Generate unrooted trees
    trees = generate_unrooted_trees(species_names)

    # Write results to file
    with open('eubt_results.txt', 'w') as output_file:
        for tree in trees:
            output_file.write(tree + '\n')

if __name__ == "__main__":
    main()
