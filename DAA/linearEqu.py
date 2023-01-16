from scipy.optimize import linprog

# define the objective function
c = [-1, 4]

# define the constraints
A = [[3, 2], [2, 5], [1, 1]]
b = [10, 20, 5]

# define the bounds on the variables
x0_bounds = (None, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')
print("\n\n")
print(res)

"""
The above code defines an objective function given by c = [-1, 4], which represents the linear function -x0 + 4x1. It also defines three constraints given by A = [[3, 2], [2, 5], [1, 1]] and b = [10, 20, 5], which represent the linear inequalities 3x0 + 2x1 <= 10, 2x0 + 5x1 <= 20, and x0 + x1 <= 5. The bounds on the variables are defined as x0_bounds = (None, None) and x1_bounds = (0, None), which means that x0 is unbounded and x1 is non-negative. Finally, the linprog() function is called with the specified objective function, constraints, bounds, and the simplex method, which returns the optimal solution.

Note that the above code uses the scipy library, which you will need to install if you don't have it already.
"""