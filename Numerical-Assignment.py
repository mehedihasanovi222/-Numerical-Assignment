import math

# Step size
h = 0.1
# Number of steps
N = 5

x_val = [0]
y_euler = [1]
y_rk4 = [1]
y_exact = [1]
abs_error_euler = [0]
abs_error_rk4 = [0]
rel_error_euler = [0]
rel_error_rk4 = [0]
accuracy_note_list = []
stability_note_list = []

# ODE function
def f(x, y):
    """
    ODE function for dy/dx = -2y
    Parameters:
        x (float)
        y (float)
    Returns:
        float
    """
    return -2 * y

# Compute step by step
for i in range(N):
    xn = x_val[-1]
    yn_e = y_euler[-1]
    yn_r = y_rk4[-1]

# Euler method
    y_next_e = yn_e + h * f(xn, yn_e)
    y_euler.append(y_next_e)

 # RK4 method
    k1 = h * f(xn, yn_r)
     k2 = h * f(xn + h/2, yn_r + k1/2)
    k3 = h * f(xn + h/2, yn_r + k2/2)
  k4 = h * f(xn + h, yn_r + k3)
    y_next_r = yn_r + (k1 + 2*k2 + 2*k3 + k4)/6
    y_rk4.append(y_next_r)

    

