from gplotLib import *
from globalVars import *

def circshift(arr, shift):
    '''
    periodic shift 
    '''
    n = len(arr)
    shift %= n  
    return np.roll(arr, shift)

def analytic(x, t_c):
    '''
    analytic solution
    '''
    return np.sin(2 * np.pi * (x - a * t_c))

from funcs import *

def upwind(u, CFL):
    u_l1 = circshift(u, 1) 
    temp = u - CFL * (u - u_l1)
    return temp

# def Lax(u, CFL):
#     u_l1 = circshift(u, 1) 
#     u_r1 = circshift(u, -1) 
#     temp = (u_r1 + u_l1) / 2 - CFL * (u_r1 - u_l1) / 2
#     return temp

def FTCS(u, CFL):
    u_l1 = circshift(u, 1) 
    u_r1 = circshift(u, -1) 
    temp = u - CFL * (u_r1 - u_l1) / 2
    return temp

def LaxWendroff(u, CFL):

    u_l1 = circshift(u, 1) 
    u_r1 = circshift(u, -1) 
    temp = u - CFL * (u_r1 - u_l1) / 2 + CFL**2 * (u_r1 - 2 * u + u_l1) / 2
    return temp

def LaxFriedrichs(u, CFL):

    u_l1 = circshift(u, 1) 
    u_r1 = circshift(u, -1) 
    temp = (u_r1 + u_l1) / 2 - CFL * (u_r1 - u_l1) / 2
    return temp

def MacCormack(u, CFL):
    r'''
    \bar{u}_j^{n+1} = u_j^n - c \left( u_{j+1}^n - u_j^n \right) \\
    u_j^{n+1} = \frac{1}{2} \left( u_j^n + \bar{u}_j^{n+1} \right) - \frac{1}{2} c \left( \bar{u}_j^{n+1} - \bar{u}_{j-1}^{n+1} \right)
    '''

    u_l1 = circshift(u, 1)
    u_r1 = circshift(u, -1)
    temp1 = u - CFL * (u_r1 - u)
    temp1_l1 = circshift(temp1, 1)
    temp2 = (u + temp1) / 2 - CFL * (temp1 - temp1_l1) / 2
    return temp2    

def LeapFrog(u, u_b1, CFL):
    r'''
    u_j^{n+1} = u_j^{n-1} - c \left( u_{j+1}^n - u_{j-1}^n \right)
    '''
    u_l1 = circshift(u, 1)
    u_r1 = circshift(u, -1)
    u_f1 = u_b1 - CFL * (u_r1 - u_l1)
    return u_f1

def upwind2(u, CFL):
    r'''
    u_j^{n+1} = u_j^n - c \left( 3 u_j^n - 4 u_{j-1}^n + u_{j-2}^n
    '''
    u_l1 = circshift(u, 1)
    u_l2 = circshift(u, 2)
    temp = u - CFL * (3 * u - 4 * u_l1 + u_l2)
    return temp

def WarmingBeam(u, CFL):
    r'''
    u_j^{n+1} = u_j^n -
    c \left( 
        u_j^n - u_{j-1}^n
    \right) - 
    \frac{1}{2} c (1-c) \left( 
        u_j^n - 2 u_{j-1}^n + u_{j-2}^n
    \right)
    '''
    u_l1 = circshift(u, 1)
    u_l2 = circshift(u, 2)
    temp = u - CFL * (u - u_l1) - 0.5 * CFL * (1 - CFL) * (u - 2 * u_l1 + u_l2)
    return temp

def AdamsBashforth(u, u_b1, CFL):
    r'''
    u_j^{n+1}=u_j^n-\frac{c}{4}\left[3\left(u_{j+1}^n-u_{j-1}^n\right)-\left(u_{j+1}^{n-1}-u_{j-1}^{n-1}\right)\right]
    '''
    u_l1 = circshift(u, 1)
    u_r1 = circshift(u, -1)
    u_b1_l1 = circshift(u_b1, 1)
    u_b1_r1 = circshift(u_b1, -1)

    u_f1 = u - CFL / 4 * (3 * (u_r1 - u_l1) - (u_b1_r1 - u_b1_l1))

    return u_f1

def numeric(previous_u_fdm,scheme_name,CFL):
    '''
    numeric solution based on previous_u_fdm (2-level finite difference method)
    '''
    if scheme_name == '1st Upwind':
        u = upwind(previous_u_fdm, CFL)
    # elif scheme_name == 'Lax':
    #     u = Lax(previous_u_fdm, CFL)
    elif scheme_name == 'FTCS':
        u = FTCS(previous_u_fdm, CFL)
    elif scheme_name == 'Lax-Wendroff':
        u = LaxWendroff(previous_u_fdm, CFL)
    elif scheme_name == 'Lax-Friedrichs':
        u = LaxFriedrichs(previous_u_fdm, CFL)
    elif scheme_name == 'MacCormack':
        u = MacCormack(previous_u_fdm, CFL)
    elif scheme_name == '2nd Upwind':
        u = upwind2(previous_u_fdm, CFL)
    elif scheme_name == 'Warming-Beam':
        u = WarmingBeam(previous_u_fdm, CFL)
    else:
        pass
    # pass
    return u

def numeric3(previous_u_fdm,previous_previous_u_fdm,scheme_name,CFL):
    '''
    numeric solution based on previous two u_fdm (3-level finite difference method)
    '''
    if scheme_name == 'Leap-Frog':
        u = LeapFrog(previous_u_fdm, previous_previous_u_fdm, CFL)
    elif scheme_name == 'Adams-Bashforth':
        u = AdamsBashforth(previous_u_fdm, previous_previous_u_fdm, CFL)

    return u