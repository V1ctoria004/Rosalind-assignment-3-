from Bio import Phylo

def parse_newick(file_path):
    with open(file_path, 'r') as file:
        return Phylo.read(file, 'newick')

# ... (rest of your code remains the same)


def generate_character_table(tree, taxa_order):
    character_table = []

    def is_leaf(node):
        return node.is_terminal()

    def get_character(node):
        character = [0] * len(taxa_order)
        for i, taxon in enumerate(taxa_order):
            if taxon in node.get_terminals():
                character[i] = 1
        return character

    for edge in tree.find_clades(order='preorder'):
        if not is_leaf(edge):
            character_table.append(get_character(edge))

    return character_table

def print_character_table(character_table):
    for row in character_table:
        print(''.join(map(str, row)))

def main():
    file_path = 'rosalind_ctbl.txt'
    tree = parse_newick(file_path)

    taxa_order = sorted([term.name for term in tree.get_terminals()])
    character_table = generate_character_table(tree, taxa_order)

    print_character_table(character_table)

if __name__ == "__main__":
    main()
