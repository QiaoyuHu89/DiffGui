import sys
sys.path.append('../')
import argparse
from utils.data import PDBProtein, parse_drug3d_mol

def main(args):
    with open(args.protein, "r") as f:
        protein_block = f.read()
    protein = PDBProtein(protein_block)
    ligand = parse_drug3d_mol(args.ligand)
    pdb_pocket_block = protein.residues_to_pdb_block(
            protein.query_residues_ligand(ligand, args.radius)
        )
    with open(args.pocket, "w") as f:
        f.write(pdb_pocket_block)


if __name__ == "__main__":
    # Useage: python extract_pockets.py --protein 3ztx_protein.pdb --ligand 3ztx_ligand.sdf --radius 10 --pocket 3ztx_pocket.pdb
    parser = argparse.ArgumentParser()
    parser.add_argument("--protein", type=str, default="3ztx_protein.pdb")
    parser.add_argument("--ligand", type=str, default="3ztx_ligand.sdf")
    parser.add_argument("--radius", type=int, default=10)
    parser.add_argument("--pocket", type=str, default="3ztx_pocket.pdb")
    args = parser.parse_args()

    main(args)
