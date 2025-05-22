gmx chi -f ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_SIM2_dt1000.pdb -s ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_0ns.gro -all -maxchi 4 -g op.log -ot op.xvg
rm histo-chi*
rm op.*
rm order.xvg
mkdir chi1
mkdir chi2
mkdir chi3
mkdir chi4
mv chi1*.xvg chi1/.
mv chi2*.xvg chi2/.
mv chi3*.xvg chi3/.
mv chi4*.xvg chi4/.
#BACKBONE DIHEDRALS
gmx chi -f ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_SIM2_dt1000.pdb -s ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_0ns.gro -all -phi
rm histo-*
rm chi.log
rm order.xvg
mkdir phi
mv phi*.xvg phi/.
gmx chi -f ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_SIM2_dt1000.pdb -s ../../../../../../LC3_MAIN_TRAJECTORIES/PROTEIN_ONLY_FITTED/preLC3B_OPLS/preLC3B_OPLS_0ns.gro -all -psi
rm histo-*
rm chi.log
rm order.xvg
mkdir psi
mv psi*.xvg psi/.
