# Linear Programing

## LP Explanation
Linear Programing is used to extract the minimum or maximum of **linear equations**. 
The cool part about linear programing is that it can handle constraints over the input arguments. 

## Mixed-integer LP: 
An extension of LP. In these problems, at least one variable takes a discrete integer value rather than continuous.
<br/>
The number of items like vehicles in an optimization problem can be represented with Mixed-integer LP.

## LP with Python:
1) Almost all the LP libraries are written in C, Fortran, or C++ because it's computationally intensive.

## Small LP problem
1) maximize: `z = 3x + 2y`
2) subject to: 
   1) `2x + 2y < 10`
   2) `x > 0`
3) Mixed-Integer: by imposing the idea that x should be discrete or integer, the LP becomes Mixed-Integer LP. 

### Notations:
1) independent variables or decision variables: x, y
2) objective function, the cost function, or just the goal: z
3) inequality constraints: 1, 2
4) Infeasible Linear Programming problem: if no solution satisfies all the constraints.
5) Unbounded LP problem: If the number of solutions is not finite.

## Python packages:
1) scipy
2) PuLP

## Installation:
https://realpython.com/linear-programming-python/#installing-scipy-and-pulp

```commandline
pip install -r requirements.txt
```
or
```commandline
python -m pip install -U git+https://github.com/coin-or/pulp
```
## References:
1) https://realpython.com/linear-programming-python/

