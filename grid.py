from mylibs import *
from globalVars import *

# set time and space domain
L = 3.0     # space domain (start from 0)
T = 20.0    # time domaim, set a large value to make animation longer 


# set grids
h      = 0.02        # grid size h
# CFL    = 0.3         # CFL number
# # CFL    = 0.6         # CFL number
# # CFL    = 1.2         # CFL number
# tau    = CFL * h / a # time step size
# Nx     = int(L / h)
# nsteps = int(T / tau)
# x      = np.arange(0, L + h, h)         # space variable, containing Nx+1 points, from 0 to L
# t      = np.arange(0, T + tau, tau)     # time variable, containing nsteps+1 points, from 0 to T
