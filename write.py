import numpy as np
import datetime
import random

def writeParticle(core,binding_f,binding_style,memb):

    with open( 'particle.txt', 'w' ) as g:
        box_max = np.max(core[:,2],axis=0)+10
        if binding_style == 'Even':
            receps = []
            ops = list(range(len(core)))
            while len(receps) < int(len(core)*binding_f):
                rch = random.choice(range(len(ops)))
                receps.append(ops[rch])
                ops.pop(rch)
        nParticles = len(core)
        g.write("#NP 10*10*20\n#second line will be skipped\n\n" )
        g.write( "{0:.0f}     atoms\n".format( nParticles) )
        g.write( "0     bonds\n")
        g.write("0    angles\n")
        g.write("0  dihedrals\n" )
        g.write("0  impropers\n\n" )
        g.write("6 atom types\n1 bond types\n1 angle types\n0  dihedral types\n0  improper types\n\n")
        g.write("{0:.2f} {1:.2f} xlo xhi\n{2:.2f} {3:.2f} ylo yhi\n{4:.2f} {5:.2f} zlo zhi".format(memb[0,0],memb[0,1],memb[1,0],memb[1,1],-2*box_max,2*box_max))
        g.write("\nAtoms\n\n")
        t=0
        while t < nParticles:
            if t in receps:
                g.write( "{0:.0f} 1 4 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, star[ t, 0 ], star[ t, 1 ], star[ t, 2 ] ) )
            else:
                g.write( "{0:.0f} 1 5 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, star[ t, 0 ], star[ t, 1 ], star[ t, 2 ] ) )
            t+=1

        g.close()
    return

def writeMembrane(data):
    box_max = np.max(data[:,2:5],axis=0)
    box_min = np.min(data[:,2:5],axis=0)
    with open( 'membrane_restart.txt', 'w' ) as g:
        nParticles = len(data)
        bonds = nParticles*(2/3)
        angles = nParticles/3
        g.write("#NP 10*10*20\n#second line will be skipped\n\n" )
        g.write( "{0:.0f}     atoms\n".format( nParticles) )
        g.write( "{0:.0f}     bonds\n".format(bonds ))
        g.write("{0:.0f}    angles\n".format( angles))
        g.write("0  dihedrals\n" )
        g.write("0  impropers\n\n" )
        g.write("5 atom types\n1 bond types\n1 angle types\n0  dihedral types\n0  improper types\n\n")
        g.write("{0:.2f} {1:.2f} xlo xhi\n{2:.2f} {3:.2f} ylo yhi\n{4:.2f} {5:.2f} zlo zhi".format(box_min[0],box_max[0],box_min[1],box_max[1],box_min[2],box_max[2]))
        g.write("\n\nMasses\n\n1 1.0\n2 1.0\n3 1.0\n4 1.0\n5 1.0\n")
        g.write("\nAtoms\n\n")
        t = 0
        for i in data:
            g.write( "{0:.0f} {1:.0f} {2:.0f} 0.0 {3:.3f} {4:.3f} {5:.3f} \n".format( t+1, t//3, i[1], i[2], i[3], i[4] ) )
            t+=1
        g.write ("\nBonds\n\n")
        t = 0
        n=0
        while n < bonds:
            g.write( "{0:.0f} 1 {1:.0f} {2:.0f} \n".format( n+1, int(t+1), int(t+2) ) )
            n+=1
            t+=1
            g.write( "{0:.0f} 1 {1:.0f} {2:.0f} \n".format( n+1, int(t+1), int(t+2) ) )
            t+=2
            n+=1
        g.write ("\nAngles\n\n")
        t = 0
        n=0
        while n < angles:
            g.write( "{0:.0f} 1 {1:.0f} {2:.0f} {3:.0f} \n".format( n+1, int(t+1), int(t+2), int(t+3) ) )
            n+=1
            t+=3

        g.close()
    return
