## Task

Consider a degree $n$ equation with a single variable: $c_{n} * x^n + c_{n-1} * x^{n-1} + \dots + c_1 * x + c_0 = 0$, where $c_{n}$, $c_{n-1}$, $\dots$, $c_{0}$ are the coefficients of the equation, and $x$ is the variable (indeterminate). It is known that all the roots of the equation are natural numbers. Additionally, it is known that any root $r$ of the equation has the property $1 \leq r \leq lim$. Furthermore, $c_{n} = 1$ (therefore $c_{n}$ does not appear in the input file largestroot.in). Calculate the largest root of the equation.

## Input data

The input data is read from the file `largestroot.in`. The first line of the file contains the number of tests, $t$. The following lines contain the tests (each test refers to an equation). For each test, the following information is provided:
* the first line of the file associated with the test contains the value $n$ (the degree of the equation)
* each of the following lines contains a coefficient of the equation in the order: $c_{n-1}$, $\dots$, $c_{0}$.

## Output data

For each test, the result (the largest root of the equation corresponding to that test) is printed on a separate line in the file `largestroot.out`. The results of the tests will be written in the file `largestroot.out` in the same order in which the tests were read from the input file.

## Constraints

$1 \leq t \leq 10$

$1 \leq n \leq 20$

$lim = 100$

$-10^{50} \leq c_{n-1}$, $\dots$, $c_{0} \leq 10^{50}$

## Example

`largestroot.in largestroot.out`

``` 
2 
4 
-9 
29 
-39 
18 
16 
-736 
248569 
-51058574 
7127315174 
-715471348256 
53300296903338 
-2997247978424004 
128130462876429813 
-4160197014559810888 
101712052492330589053 
-1840693695109078832542 
23974924768088488764452 
-215121428625760065465800 
1240124343089704479058400 
-4062170275292596661376000 
5656841549245342310400000 
3 
```