#!/usr/bin/env python3
from pyscf import gto, scf, mp
import sys
from fileutils import dump
import h5py

mol = gto.Mole()
mol.verbose = 10
mol.atom = f"geom_{sys.argv[1]}.xyz"
mol.basis = "ccpvtz"
mol.unit = "ANG"
mol.build()

mf = scf.RHF(mol)
# determine the output of mf.kernel()
mf.kernel()

conv = mf.converged
e_tot = mf.e_tot
mo_energy = mf.mo_energy
mo_coeff = mf.mo_coeff

dataout = {}
dataout["e_tot"] = e_tot
dataout["conv"] = conv
dump(dataout, f"data/hf_geom_{sys.argv[1]}.json")

with h5py.File(f"data/hf_geom_{sys.argv[1]}.h5", "w") as f:
    f.create_dataset("mo_energy", data=mo_energy)
    f.create_dataset("mo_coeff", data=mo_coeff)