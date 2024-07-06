Alexandru has at his disposal a square array of dimension $n$ with integer numbers and $k$ equations of type $I$ and $II$. The type $I$ equations are of the form: $ax+b=c$, with $a, b, c$ being natural numbers, while type $II$ equations are of the form: $ax^2+bx+c=d$, with $a, b, c, d$ being natural numbers.

Alexandru aims to determine for each type of equation: their number and how many of them have roots in the given array.

# Task

Write a program that determines the number of type $I$ equations, how many of these have exactly one root in the array, the number of type $II$ equations, and how many of these have exactly both roots in the array.

# Input data

The input file `ec.in` will contain: on the first line the natural numbers $n$ and $k$ separated by a space, on the next $n$ lines the elements of the array separated by a space, and on the following $k$ lines the equations in the form given in the statement, one per line.

# Output data

The output file `ec.out` will contain on the first line two numbers separated by a space representing the number of type $I$ equations and the number of type $I$ equations that have exactly one root found in the array, and on the second line also two numbers separated by a space representing the number of type $II$ equations and the number of type $II$ equations with exactly two roots, both roots found in the array.

# Constraints and clarifications

* $1 \leq n \leq 500$
* $1 \leq n \leq 1 \ 000$
* The elements of the array are integers with a maximum of $4$ digits each
* For each type $I$ equation - $a,b,c$ will be specified, even if they have the value $0$ or $1$, (for example $x + 2 = 3$ will appear as $1x+2=3$)
* For each type $II$ equation - $a,b,c,d$ will be specified, even if they have the value $0$ or $1$, (for example $x^2+1=3$ will appear as $1x^2+0x+1=3$)
* For type $I$ equations - $a,b,c$ are natural numbers with a maximum of $4$ digits
* For type $II$ equations - $a,b,c,d$ are natural numbers with a maximum of $4$ digits
* $10\%$ of the score will be awarded for the number of type $I$ equations, $30\%$ for how many of them have exactly one root in the array, $20\%$ for the number of type $II$ equations and $40\%$ for how many of them have exactly two roots in the array

# Example

`ec.in`
```
2 5
1 2
2 -1
1x+0=0
20x^2+40x+20=0
101x+200=402
2x^2+1x+4=0
1x^2+1x+3=5
```

`ec.out`
```
2 1
3 1
```

# Explanation

The first equation is of type $I$ and has the root $0$, which is not found in the array.

The second equation is of type $II$ and has two equal roots $-1$, which are found in the array.

The third equation is of type $I$ and has the root $2$, which is found in the array.

The fourth equation is of type $II$ and does not have its roots in the array.

The fifth equation is of type $II$ and has roots $-2$ and $1$, but not both in the array.