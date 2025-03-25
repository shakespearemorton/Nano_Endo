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
                g.write( "{0:.0f} 1 4 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, core[ t, 0 ], core[ t, 1 ], core[ t, 2 ] ) )
            else:
                g.write( "{0:.0f} 1 5 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, core[ t, 0 ], core[ t, 1 ], core[ t, 2 ] ) )
            t+=1

        g.close()
    return

def writeMembrane(pos,receptor_f,boxx,boxy,boxz):
    with open( 'membrane.txt', 'w' ) as g:
        nParticles = len(pos)
        bonds = nParticles*(2/3)
        angles = nParticles/3
        g.write("#NP 10*10*20\n#second line will be skipped\n\n" )
        g.write( "{0:.0f}     atoms\n".format( nParticles) )
        g.write( "{0:.0f}     bonds\n".format(bonds ))
        g.write("{0:.0f}    angles\n".format( angles))
        g.write("0  dihedrals\n" )
        g.write("0  impropers\n\n" )
        g.write("7 atom types\n1 bond types\n1 angle types\n0  dihedral types\n0  improper types\n\n")
        g.write("0 {0:.2f} xlo xhi\n0 {1:.2f} ylo yhi\n-{2:.2f} {2:.2f} zlo zhi".format(boxx,boxy,boxz/2))
        g.write("\n\nMasses\n\n1 1.0\n2 1.0\n3 1.0\n4 1.0\n5 1.0\n6 1.0\n7 1.0\n")
        g.write("\nAtoms\n\n")
        t=0
        receps = []
        ops = list(range(len(pos)))
        while len(receps) < int(len(pos)*receptor_f):
            rch = random.choice(range(len(ops)))
            receps.append(ops[rch])
            ops.pop(rch)
        mol = 1
        while t < nParticles:
            if int(t/3) in receps:
                g.write( "{0:.0f} {4:.0f} 3 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, pos[ t, 0 ], pos[ t, 1 ], pos[ t, 2 ],mol ) )
                t+=1
            else:
                g.write( "{0:.0f} {4:.0f}  1 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, pos[ t, 0 ], pos[ t, 1 ], pos[ t, 2 ],mol ) )
                t+=1
            g.write( "{0:.0f} {4:.0f} 2 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, pos[ t, 0 ], pos[ t, 1 ], pos[ t, 2 ],mol ) )
            t+=1
            g.write( "{0:.0f} {4:.0f} 2 0.0 {1:.3f} {2:.3f} {3:.3f} \n".format( t+1, pos[ t, 0 ], pos[ t, 1 ], pos[ t, 2 ],mol ) )
            t+=1
            mol+=1
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
