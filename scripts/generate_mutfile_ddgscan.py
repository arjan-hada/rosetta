import argparse
import pathlib

def generate_mutfile_ddgscan(protein_sequence, output_file):
    """
    Generate a mutfile in the format required by Rosetta cartesian_ddg protocol.
    """
    protein_length = len(protein_sequence)

    with open(output_file, 'w') as mutfile:
        mutfile.write(f'total {protein_length * 20}\n')
            
        # Define the amino acid alphabet (one-letter codes)
        amino_acids = "ACDEFGHIKLMNPQRSTVWY"

        # Iterate through each position in the protein sequence
        for position in range(len(protein_sequence)):

            # Generate mutants for each amino acid in the alphabet
            for aa in amino_acids:
                mutfile.write(f'1\n')
                mutfile.write(f'{protein_sequence[position]} {position+1} {aa}\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Rosetta mutfile for all 20 amino acid substitutions at each position.")
    parser.add_argument("--protein_sequence", type=str, help="Protein sequence for mutation")
    parser.add_argument("--output_mutfile", type=pathlib.Path, help="Output mutfile containing energy scores")

    args = parser.parse_args()

    generate_mutfile_ddgscan(args.protein_sequence, args.output_mutfile)
    print(f"Mutfile generated: {args.output_mutfile}")