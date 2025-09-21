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


