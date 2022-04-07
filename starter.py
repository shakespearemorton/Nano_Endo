from particle import *
from write import *
from tab_pot import *

options = [.2,.5,.8]
options2 = [2,5,8]
sphereRad = 4.3
ppsa = 1
Wc = 1.5
Epsilon = options2[REPSILON]
binding_f = options[RFRAC]
binding_style = 'Even'

memb_size = np.loadtxt('48_membrane.txt',skiprows=15,usecols=(0,1),max_rows=3)
memb = np.loadtxt('48_membrane.txt',skiprows=3,usecols=(0),max_rows=1)

core = sphere(sphereRad,1)
core[:,2] += sphereRad+1

writeParticle(core,binding_f,binding_style,memb_size)

tabs(Wc,Epsilon)
