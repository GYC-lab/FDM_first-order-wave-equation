# @file   main.py
# @author Yuchen Ge
# @time   10/21/23 11:08:52
# @desc   CFD HW3

from mylibs import *
from myGUI import *
from funcs import *
from globalVars import *
from grid import *

def gui_start():
    init_window = Tk()  
    WAVE1D = MY_GUI(init_window)
    WAVE1D.init_grid()
    WAVE1D.init_boundary()
    WAVE1D.set_init_window()
    WAVE1D.draw_true()             # draw the figure
    init_window.mainloop()  # keep window running

if __name__ == '__main__':
    gui_start()
