import control as ctrl
import matplotlib.pyplot as plt
import math
import numpy as np
G_ref = ctrl.tf([0.25], [0.003, 0.0515, 0.2, 0.25])
ctrl.root_locus(G_ref)
plt.plot(-1.5 , 1.0 , "ro" , markersize =8)
plt.plot(-2.0 , -1.0 , "ro" , markersize =8)
plt.text(-1.5 , 1.0 , "P1" , va = "bottom")
plt.text( -2.0 , -1.0 , "P2" , va = "bottom")
plt.xlabel( "Parte real") ; plt . ylabel ("Parte imaginaria")
plt.grid( True )
plt.show()