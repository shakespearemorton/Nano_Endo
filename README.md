# Nano_Endo
Endocytosis of nanoparticles using the Cooke-Deserno potential.

## Step 1: Create a membrane

Run **membrane.py**, and set the size of your membrane. The size is related to the box size of the system, and lipids are placed on an HCP lattice.
Larger membranes may need more time to equilibrate, or may be unstable. 

## Step 2: Equilibrate Membrane

Use the LAMMPS code provided, **equil.in** to equilibrate the membrane. Again, larger membranes take longer to relax. If you do create your own membrane, please be sure to change the name in **starter.py** and **lipid.in**.

## Step 3: Put the system together

**starter.py** will create a spherical nanoparticle with n ligands and ε interaction strength. It is currently set up to be run as a batch job, reproducing the results from the following paper: <div class="csl-entry">Vácha, R., Martinez-Veracoechea, F. J., &#38; Frenkel, D. (2011). Receptor-mediated endocytosis of nanoparticles of various shapes. <i>Nano Letters</i>, <i>11</i>(12), 5391–5395. https://doi.org/10.1021/nl2030213</div>

These files can be created in batch and by running the *collect.sh* file.

Feel free to create your own nanoparticles with various distributions of ligands on the surface.

## Step 4: Run in LAMMPS

The **lipid.in** file will run the membrane and particle in LAMMPS.
