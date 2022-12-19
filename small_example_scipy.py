from scipy.optimize import linprog

obj = [-1, -2]  # -z = -x -2y (coefficients)

lhs_ineq = [[2, 1],  # 2x + y < 20
            [-4, 5], ]  # -4x + 5y <10
rhs_ineq = [20,  # 20 of the previous equation
            10]  # 10 the previous equation

lhs_eq = [[-1, 5]]  # -x + 5y =15

rhs_eq = [15]

bounds = [(0, float("inf")),  # Bounds of x
          (0, float("inf"))]  # Bounds of y
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bounds,
              method="revised simplex")
