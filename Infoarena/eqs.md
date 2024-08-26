## Equations

We consider equations of the form: $a_1 *x_1^3 + a_2 *x_2^3 + a_3 *x_3^3 + a_4 *x_4^3 + a_5 *x_5^3 = 0$. All the unknowns appear to the third power. The coefficients $a_1 ,a_2 ,a_3 ,a_4 ,a_5$ are given integers from the closed interval $[-50,+50]$. A solution is considered to be a pentuple $(x_1 ,x_2 ,x_3 ,x_4 ,x_5)$ that satisfies the equation.

##  Task

Find the number of solutions of the equation, for which the values of the unknowns are non-zero integers from the closed interval $[-50,+50]$.

##  Input data

The first line of the input file `eqs.in` contains the 5 integer coefficients $a_1 ,a_2 ,a_3 ,a_4 ,a_5$ separated by a space.

##  Output data

The first line of the output file `eqs.out` will contain the number of solutions.

##  Constraints and clarifications

- The coefficients of the equation are integers from the interval $[-50, +50]$
- A program that works perfectly for $a_4 = 0$ $a_5 = 0$ will obtain at least 20 points.
- A program that works perfectly for $a_5 = 0$ will obtain at least 40 points.

##  Example

`eqs.in`
```
37 29 41 43 47
```

`eqs.out`
```
654
```