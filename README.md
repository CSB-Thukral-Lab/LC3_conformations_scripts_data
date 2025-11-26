# A novel lipid-triggered allosteric site modulates LC3-LIR receptor binding activity
This repository contains custom scripts [Python code and Jupyter notebooks], data and plots from the MD Simulations of LC3 proteins in cytosolic state [alias: pre], membrane-bound apo state [alias: unb/unbound] and membrane-bound state with p62-LIR receptor [alias: bnd/bound]. 
In addition, the repository contains data obtained from the in-silico screening of mutations at the allosteric site. 
Source data are compiled according to the main figures presented in the paper. The supplementary videos related to the manuscript are also deposited.


Here is the list of important data/scripts that can be accessed (grouped according to figure panels).

##1. Intra-protein contact data [Related to Figure 1d, 2h and their associated SI]
    * The scripts used for computing intra-protein contacts is provided here 'scripts/intra_protein_contacts' 
    * The notebook used to compute state-specific contacts is here scripts/intra_protein_contacts/state_specific_contacts'
    * The associated data can be located here data/intra_protein_contacts
    * Associated plots can be accessed here plots/intra_protein_contacts
##2. Geometric analysis [Related to Figure 1e, 3c, 3e and associated SI]
    * The notebooks related to geometric analysis (distance/angle calculations) are provided here 'scripts/geometric_analysis'
    * Associated plots are saved here 'plots/geometric_analysis'
##3. Pocket volume associated calculations [Related to Figure 2C and their associated SI]
    * Scripts related to the inter-pocket distance calculation and construction of a 2D-probability landscape are here 
        * 'scripts/pocket_volume/four_point_distance_calculations.ipynb'
        * 'scripts/pocket_volume/pv_vs_distance.ipynb'
    * Data associated with the pocket volume: 'data/pocket_volume'
    * Plots: data/plots/pocket_volume
##4. Dihedral associated data [Related to Figure 1f to 1i and associated SI]
    * All raw data related to dihedral angles, rotamers and orderness assignment can be found here 'data/dihedrals/raw_data' 
    * Notebook for computing Shannon entropy 'scripts/dihedrals/dihedral_entropy_calculations'
    * Notebook for computing rotamer shift 'scripts/dihedrals/rotamer_shift'
    * Plots: 'plots/dihedrals/dihedral_entropy_calculations' and 'plots/dihedrals/rotamer_shift'
##5. Net Communication [Related to Figure 2e, 2f and associated SI]
    * All raw data/custom scripts related to the calculation of Mutual Information of backbone+sidechain dihedrals/rotamers/orderness states can be located here 'data/dihedrals/net_communication'. The subdirectories are grouped according to the LC3 states. 
    * Important notebooks
        * Notebook for computing residue-wise communication strength 'scripts/dihedrals/net_comm_analysis.ipynb'
        * Notebook for computing the contribution of each LC3 segment to the overall net communication 'scripts/dihedrals/net_comm_contribution.ipynb'
    * Related plots: 'plots/dihedrals/net_communication'
##6. Screening of mutant candidates [Related to Figure 3c, 3e]
    * Probing distance calculations for the allosteric site are provided here '/scripts/TRIAD_MUTANT_CANDIDATES/triad_distance_checks.ipynb'
    * Plots '/plots/TRIAD_MUTANT_CANDIDATES'



 
