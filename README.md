# Assignment: Implement Euler’s Method and Runge-Kutta (RK4) for solving the ODE dy/dx=−2y,y(0)=1.Compare numerical results with the exact solution y = e-2x. Analyze accuracy and stabilit

---

## Problem Statement

We need to solve the following initial value problem (IVP):

$$
\frac{dy}{dx} = -2y, \quad y(0) = 1
$$

* Implement **Euler’s Method** and **Runge-Kutta 4th Order (RK4)**.
* Compare numerical solutions with the **exact solution**:

  $$
  y(x) = e^{-2x}
  $$
* Analyze **accuracy** and **stability** of both methods.

---

## Theory

### 1. Euler’s Method

Euler’s method is a *first-order numerical method*.
The update formula is:

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

* Easy to implement.
* Accuracy: *O(h)* (linear).
* Stability: requires *small step size* for reliable results.
Write to Numerical Methods Assignment

### 2. Runge-Kutta 4th Order (RK4)

RK4 is a *fourth-order method*.
The formula is:

$$
\begin{aligned}
k_1 &= h f(x_n, y_n) \\
k_2 &= h f\Big(x_n + \tfrac{h}{2}, y_n + \tfrac{k_1}{2}\Big) \\
k_3 &= h f\Big(x_n + \tfrac{h}{2}, y_n + \tfrac{k_2}{2}\Big) \\
k_4 &= h f(x_n + h, y_n + k_3) \\
y_{n+1} &= y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}
$$

* More complex, but very accurate.
* Accuracy: *O(h⁴)* (much better).
* More stable for larger step sizes.

---

## Python Code

```python
import math

# Step size and number of steps
h = 0.1
N = 20   # solve up to x = 2.0

# Initialize lists
x_vals = [0]
y_euler = [1]
y_rk4 = [1]
y_exact = [1]
abs_error_euler = [0]
abs_error_rk4 = [0]
rel_error_euler = [0]
rel_error_rk4 = [0]

# ODE function: dy/dx = -2y
def f(x, y):
    return -2 * y

# Compute step by step
for i in range(N):
    x_n = x_vals[-1]
    y_n_e = y_euler[-1]
    y_n_r = y_rk4[-1]

# Euler method
    y_next_e = y_n_e + h * f(x_n, y_n_e)
    y_euler.append(y_next_e)


