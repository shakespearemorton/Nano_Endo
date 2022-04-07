from particle import *
from bilayer import *
from write import *
import random
from tab_pot import *

Timesteps = 10000000
receptor_f = 0.50
Box = 60
Wc = 1.5
Sigma = 1
Epsilon = 1

memb, boxx, boxy = hexLipids(Box)
writeMembrane(memb,receptor_f, boxx, boxy, 20)

tabs(Wc,Sigma,Epsilon)
