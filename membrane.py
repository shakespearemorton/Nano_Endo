from particle import *
from bilayer import *
from write import *
import random
from tab_pot import *

receptor_f = 0.50
Box = 60
Wc = 1.5

memb, boxx, boxy = hexLipids(Box)
writeMembrane(memb,receptor_f, boxx, boxy, 20)

tabs(Wc)
