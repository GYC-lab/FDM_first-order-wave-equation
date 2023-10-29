
# Info

- author : Yuchen Ge
- time   : 10/21/23 
- desc   : CFD HW3

# Usage

- Numerical solutions of the first-order one-way wave equation are obtained by the finite difference method (FDM) with the following schemes:
  - 1st Upwind scheme
  - 2nd Upwind scheme
  - FTCS scheme
  - Lax-Friedrichs scheme
  - Lax-Wendroff scheme
  - MacCormack scheme
  - Warming-Beam scheme
  - Leapfrog scheme
  - Adams-Bashforth scheme
- You are supposed to select the FDM scheme first before selcting CFL number
- The time-series of solution $u(x,t)$ is not saved, only the necessary data for animation is saved temporarily
- The main function is in the file `main.py`
- The FDM algorithms are called by `animate_both()` function in `myGUI.py`
