import numpy as np
import math
from scipy.spatial.transform import Rotation

def rescale(r1,r):
  mod = np.sqrt( ( r1**2 ).sum() )
  if r1[0] == 0:
        teta = np.pi/2
  else:
    teta = np.arctan( r1[ 1 ]  / r1[ 0 ] )
    
  if r1[ 0 ] > 0:
    phi = np.arccos( r1[ 2 ] / mod )
  else:
    phi = 2.0 * np.pi - np.arccos( r1[ 2 ] / mod )
  rvec = surface( phi,teta,r)

  return rvec

def surface( p, t,r):
  x = r * np.sin( p ) * np.cos( t )
  y = r * np.sin( p ) * np.sin( t )
  z = r * np.cos( p )
  return (  [x, y, z]  )        

def sphere(r,ppsa,use = 0,num = 0):
    ''' Create a sphere using a Fibonnaci spiral'''
    sa = 4*np.pi*r**2
    if use == 0:
        num = sa * ppsa
    points = []
    phi = math.pi * (3. - math.sqrt(5.))

    for i in range(int(num)):
        y = 1 - (i / float(num - 1)) * 2 
        radius = math.sqrt(1 - y * y)
        theta = phi * i 
        x = math.cos(theta) * radius
        z = math.sin(theta) * radius
        points.append(rescale(np.array([x,y,z]),r))

    return np.array(points)