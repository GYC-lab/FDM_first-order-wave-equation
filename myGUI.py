from mylibs import *
from funcs import *
from grid import *
from globalVars import *

class MY_GUI():
    def __init__(self, root):

        self.root     = root
        self.interval = ginterval
        self.fig      = plt.figure(dpi=100)
        self.ax       = self.fig.add_subplot(xlim=(0, 3), ylim=(-1, 1))

        self.canvas      = None
        self.line        = None
        self.line1       = None
        self.line2       = None
        self.scheme_name = ''
        self.fontsize    = 26
        self.fontsize2   = 30
        self.customFont = Font(family="Times New Roman", size=18, weight='bold')
        self.customFont2 = Font(family="Times New Roman", size=12)

    def set_init_window(self):
        '''
        set GUI window
        '''

        self.history = []
        self.nowHistory = -1
        self.root.title("FDM of first-order wave equation by Ge Yuchen")  # name of window
        self.root.geometry('1080x720+800+20')       # position of window
        self.root["bg"] = "#EEEEEE"                 # color of background

        # set the menu
        menubar    = Menu(self.root)
        fmenu      = Menu(menubar, tearoff=False)
        emenu      = Menu(menubar, tearoff=False)
        # mainDesign = Menu(emenu, tearoff=False)
        # CFLSet     = Menu(emenu, tearoff=False)

        # set the scheme menu
        # mainDesign.add_command(label='Lax', command=self.draw_Lax)
        # mainDesign.add_command(label='1st Upwind (1)', command=self.draw_upwind)
        # mainDesign.add_command(label='2nd Upwind (2)', command=self.draw_upwind2)
        # mainDesign.add_command(label='FTCS (2)', command=self.draw_FTCS)
        # mainDesign.add_command(label='Lax-Friedrichs (1)', command=self.draw_LaxFriedrichs)
        # mainDesign.add_command(label='Lax-Wendroff (2)', command=self.draw_LaxWendroff)
        # mainDesign.add_command(label='MacCormack (2)', command=self.draw_MacCormack)
        # mainDesign.add_command(label='Leap-Frog (2)', command=self.draw_LeapFrog)
        # mainDesign.add_command(label='Warming-Beam (2)', command=self.draw_WarmingBeam)

        button_frame_schme = Frame(self.root)
        button_frame_schme.pack(side=LEFT,anchor='n')
        scheme1 = Button(button_frame_schme, text='1st Upwind (1)', command=self.draw_upwind, width=20, height=2, font=self.customFont2)
        scheme1.pack(side=TOP, padx=5, pady=5)
        scheme2 = Button(button_frame_schme, text='2nd Upwind (2)', command=self.draw_upwind2, width=20, height=2, font=self.customFont2)
        scheme2.pack(side=TOP, padx=5, pady=5)
        scheme3 = Button(button_frame_schme, text='FTCS (2)', command=self.draw_FTCS, width=20, height=2, font=self.customFont2)
        scheme3.pack(side=TOP, padx=5, pady=5)
        scheme4 = Button(button_frame_schme, text='Lax-Friedrichs (1)', command=self.draw_LaxFriedrichs, width=20, height=2, font=self.customFont2)
        scheme4.pack(side=TOP, padx=5, pady=5)
        scheme5 = Button(button_frame_schme, text='Lax-Wendroff (2)', command=self.draw_LaxWendroff, width=20, height=2, font=self.customFont2)
        scheme5.pack(side=TOP, padx=5, pady=5)
        scheme6 = Button(button_frame_schme, text='MacCormack (2)', command=self.draw_MacCormack, width=20, height=2, font=self.customFont2)
        scheme6.pack(side=TOP, padx=5, pady=5)
        scheme8 = Button(button_frame_schme, text='Warming-Beam (2)', command=self.draw_WarmingBeam, width=20, height=2, font=self.customFont2)
        scheme8.pack(side=TOP, padx=5, pady=5)
        scheme7 = Button(button_frame_schme, text='Leap-Frog (2)', command=self.draw_LeapFrog, width=20, height=2, font=self.customFont2)
        scheme7.pack(side=TOP, padx=5, pady=5)
        scheme9 = Button(button_frame_schme, text='Adams-Bashforth (2)', command=self.draw_AdamsBashforth, width=20, height=2, font=self.customFont2)
        scheme9.pack(side=TOP, padx=5, pady=5)

        button_frame_CFL = Frame(self.root)
        button_frame_CFL.pack(side=LEFT,anchor='n')
        CFLset1 = Button(button_frame_CFL, text='CFL = 0.3', command=self.set_CFL_03, width=10, height=2, font=self.customFont2)
        CFLset1.pack(side=TOP, padx=5, pady=5)
        CFLset2 = Button(button_frame_CFL, text='CFL = 0.6', command=self.set_CFL_06, width=10, height=2, font=self.customFont2)
        CFLset2.pack(side=TOP, padx=5, pady=5)
        CFLset3 = Button(button_frame_CFL, text='CFL = 1.2', command=self.set_CFL_12, width=10, height=2, font=self.customFont2)
        CFLset3.pack(side=TOP, padx=5, pady=5)
        
        # # set the self.CFL menu
        # CFLSet.add_command(label='0.3', command=self.set_CFL_03)
        # CFLSet.add_command(label='0.6', command=self.set_CFL_06)
        # CFLSet.add_command(label='1.0', command=self.set_CFL_10)
        # CFLSet.add_command(label='1.2', command=self.set_CFL_12)
        
        # add the menu to the window
        menubar.add_cascade(label="File", menu=fmenu)
        # menubar.add_cascade(label="Scheme", menu=mainDesign)
        # menubar.add_cascade(label="CFL", menu=CFLSet)

        self.root.config(menu=menubar)

        # button_frame = Frame(self.root)
        # button_frame.pack(side=RIGHT,anchor='n')

        reset_button = Button(button_frame_CFL, text='Reset', command=self.reset, width=10, height=2, font=self.customFont2)
        reset_button.pack(side=TOP, padx=5, pady=5)
        
        quit_button = Button(button_frame_CFL, text="Quit", command=self.root.quit, width=10, height=2, font=self.customFont2)
        quit_button.pack(side=TOP, padx=5, pady=5)

    def init_grid(self):
        '''
        initialize the grid
        '''
        self.CFL    = 0.3         # self.CFL number
        self.tau    = self.CFL * h / a # time step size
        self.Nx     = int(L / h)
        self.nsteps = int(T / self.tau)
        self.x      = np.arange(0, L + h, h)         # space variable, containing Nx+1 points, from 0 to L
        self.t      = np.arange(0, T + self.tau, self.tau)     # time variable, containing self.nsteps+1 points, from 0 to self.t

    def init_boundary(self):
        '''
        initialize the boundary condition
        '''
        self.u  = np.zeros(self.Nx + 1)
        self.u0 = np.sin(2 * np.pi * self.x)
        self.u0_f1 = upwind(self.u0, self.CFL) # u0_f1 is the next step of u0

    def init_true(self):
        '''
        initialize the true solution
        '''
        self.line.set_data([], [])
        
    def init_both(self):
        '''
        initialize the true solution as well as the numerical solution
        '''
        self.line1.set_data([], [])
        self.line2.set_data([], [])

    def init_anim(self):
        '''
        initialize the previous animation
        '''
        # clear the previous animation
        self.anim.event_source.stop()   # stop the previous animation
        self.remove_line()              # remove the previous line

        # add another line to the figure
        self.line1, = self.ax.plot([], [])
        self.line2, = self.ax.plot([], [])

    def update_timeStep(self):
        '''
        update the time step size after changing the CFL number
        '''

        self.tau = self.CFL * h / a # time step size
        self.t   = np.arange(0, T + self.tau, self.tau)

    def set_line_style(self):
        '''
        set the style of the line 1
        '''
        self.line.set_color('red')
        self.line.set_linewidth(2)
    
    def set_axis_style(self):
        '''
        set the style of the axis
        '''
        self.ax.set_xlim(0, 3)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_xlabel('$x$', fontsize=self.fontsize2)
        self.ax.set_ylabel('$u$', fontsize=self.fontsize2)
        self.ax.set_aspect('equal')
        # self.ax.set_title('$t = %.2f$'% self.t[i], loc='center', fontsize=self.fontsize)

    def set_ticks_style(self):
        '''
        set the style of the ticks
        '''
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
        self.ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5/5))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
        self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        self.ax.tick_params(which='major', width=1.0)
        self.ax.tick_params(which='major', length=10)
        self.ax.tick_params(which='minor', width=1.0, labelsize=self.fontsize)
        self.ax.tick_params(which='minor', length=5,    labelsize=self.fontsize, labelcolor='0.25')
        self.ax.tick_params(axis='both', which='major', labelsize=self.fontsize,direction='in')
        self.ax.tick_params(axis='both', which='minor', labelsize=self.fontsize,direction='in')

        # remove the original tick of x axis
        format_decimal_x(precision=1)

        self.ax.grid(linestyle='-.', linewidth=0.5, color='.25', zorder=-10)

    def set_line2_style(self):
        '''
        set the style of the line 2
        '''

        self.line1.set_color('r')
        self.line1.set_linewidth(2)

        self.line2.set_color('b')
        self.line2.set_linewidth(2)
        self.line2.set_marker('o')
        self.line2.set_markevery(1)

    def remove_line(self):
        '''
        remove the previous line if it exists
        '''
        if self.line in self.ax.lines:
            self.line.remove()
        if self.line1 in self.ax.lines:
            self.line1.remove()
        if self.line2 in self.ax.lines:
            self.line2.remove()

    def animate_true(self,i):
        '''
        display the true solution
        '''

        # display analytic solution
        u_true = analytic(self.x, self.t[i])
        
        # set style of line 1
        self.line.set_data(self.x, u_true)
        self.set_line_style()
        self.set_axis_style()
        self.set_ticks_style()

        # set title to display current time
        self.ax.set_title('$t = %.2f$'% self.t[i], loc='center', fontsize=self.fontsize)

    def animate_both(self,i):
        '''
        display the true solution as well as the numerical solution
        '''

        global previous_u_fdm, previous_previous_u_fdm

        if self.scheme_name in ['Leap-Frog', 'Adams-Bashforth']:

            # start from the second step
            if i == 0: 
                previous_u_fdm          = self.u0_f1
                previous_previous_u_fdm = self.u0
                
            u_true = analytic(self.x, self.t[i+2])
            self.ax.set_title('$t = %.2f$'% self.t[i+2], loc='center', fontsize=self.fontsize)

            u_fdm = numeric3(previous_u_fdm, previous_previous_u_fdm, self.scheme_name, self.CFL)
        
            # set style of line 1
            self.line1.set_data(self.x, u_true)
            self.line2.set_data(self.x, u_fdm)
            self.set_line_style()

            # set style of line 2
            self.set_line2_style()
            self.set_axis_style()
            self.set_ticks_style()

            # Upadte 
            previous_previous_u_fdm = previous_u_fdm
            previous_u_fdm          = u_fdm
            
        else:

            # start from the first step
            if i == 0:
                previous_u_fdm = self.u0

            u_true = analytic(self.x, self.t[i])
            self.ax.set_title('$t = %.2f$'% self.t[i], loc='center', fontsize=self.fontsize)

            u_fdm = numeric(previous_u_fdm, self.scheme_name, self.CFL)
            
            # set style of line 1
            self.line1.set_data(self.x, u_true)
            self.line2.set_data(self.x, u_fdm)
            self.set_line_style()

            # set style of line 2
            self.set_line2_style()
            self.set_axis_style()
            self.set_ticks_style()

            # Upadte the u_fdm
            previous_u_fdm = u_fdm

    def reset(self):
        '''
        stop current animation and reset the figure to the initial state
        '''
        self.anim.event_source.stop()   # stop the previous animation
        self.remove_line()

        self.CFL = 0.3
        self.update_timeStep()
        
        self.line, = self.ax.plot([], [])
        self.label.config(text="dx = %.2f, dt = %.3f" % (h, self.tau))
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.anim = animation.FuncAnimation(self.fig, self.animate_true, init_func=self.init_true, frames=self.nsteps, interval=self.interval, blit=False, repeat=True)
        
        self.canvas.draw()

    def draw_canvas(self):
        '''
        draw the canvas based on the scheme name for different schemes
        '''
        self.init_anim()
        self.label.config(text="dx = %.2f, CFL = %.2f, dt = %.3f, scheme = %s" % (h, self.CFL, self.tau, self.scheme_name))
        self.anim = animation.FuncAnimation(self.fig, self.animate_both, init_func=self.init_both, frames=self.nsteps, interval=self.interval, blit=False, repeat=True)
    
        self.canvas.draw()       

    def draw_true(self):
        '''
        initialize the canvas and draw the true solution
        '''

        self.line, = self.ax.plot([], [])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

        # add label above the figure
        self.label = Label(master=self.root, text="dx = %.2f, dt = %.3f"%(h,self.tau), \
                      font=self.customFont)
        self.label.pack(side=TOP)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.anim = animation.FuncAnimation(self.fig, self.animate_true, init_func=self.init_true, frames=self.nsteps, interval=self.interval, blit=False, repeat=True)
        
        self.canvas.draw()

    # def draw_Lax(self):
    #     '''
    #     compare Lax scheme with true solution
    #     '''
    #     self.scheme_name = 'Lax'
    #     self.draw_canvas()

    def draw_upwind(self):
        '''
        compare upwind scheme with true solution
        '''
        self.scheme_name = '1st Upwind'
        self.draw_canvas()
    
    def draw_FTCS(self):
        '''
        compare FTCS scheme with true solution
        '''
        self.scheme_name = 'FTCS'
        self.draw_canvas()

    def draw_LaxWendroff(self):
        '''
        compare Lax-Wendroff scheme with true solution
        '''
        self.scheme_name = 'Lax-Wendroff'
        self.draw_canvas()

    def draw_LaxFriedrichs(self):
        '''
        compare Lax-Friedrichs scheme with true solution
        '''
        self.scheme_name = 'Lax-Friedrichs'
        self.draw_canvas()

    def draw_MacCormack(self):
        '''
        compare MacCormack scheme with true solution
        '''
        self.scheme_name = 'MacCormack'
        self.draw_canvas()

    def draw_upwind2(self):
        '''
        '''
        self.scheme_name = '2nd Upwind'
        self.draw_canvas()

    def draw_LeapFrog(self):
        '''
        '''
        self.scheme_name = 'Leap-Frog'
        self.draw_canvas()

    def draw_WarmingBeam(self):
        '''
        '''
        self.scheme_name = 'Warming-Beam'
        self.draw_canvas()

    def draw_AdamsBashforth(self):
        '''
        '''
        self.scheme_name = 'Adams-Bashforth'
        self.draw_canvas()

    def set_CFL_03(self):
        self.CFL = 0.3
        self.update_timeStep()
        self.draw_canvas()
        
    def set_CFL_06(self):
        self.CFL = 0.6
        self.update_timeStep()
        self.draw_canvas()

    def set_CFL_10(self):
        self.CFL = 1.0
        self.update_timeStep()
        self.draw_canvas()

    def set_CFL_12(self):
        self.CFL = 1.2
        self.update_timeStep()
        self.draw_canvas()
