
fig_path    = '../figs/'
data_path   = './data/'
color_list  = ["#D20000", "#2d2dff",'#00D200',"#FF00FF"]
style_list  = ['-', '--', '-.', ':']
symbol_list = ['o', 's', '^', 'v', '>', '<', 'p', '*', 'h', 'H', 'D', 'd']
choice_dict = {0: 'upwind', 1: 'Lax', 2: 'FTCS', 3: 'LaxWendroff', 4: 'LaxFriedrichs', 5: 'MacCormack'}

a          = 1.0     # wave speed
choice     = 2  # 0: upwind, 1: Lax, 2: FTCS, 3: LaxWendroff, 4: LaxFriedrichs, 5: MacCormack
ginterval  = 20

