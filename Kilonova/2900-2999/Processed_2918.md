Given $N$ equations of both the first and second degree. Each equation is provided as a string that ends with a newline character, one per line, in the following format:
```
Ax^2+Bx+C=0
Dx+E=0
```
where $A$, $B$, $C$, $D$, $E$ are non-zero natural numbers.
Knowing $M$ natural numbers $v_1$, $v_2$, $\dots$, $v_M$, we want to determine how many first-degree equations we have and how many of the $N$ equations have at least one solution whose absolute value is in the array $v$.

# Task

Knowing $N$ - the number of equations, the strings for the $N$ equations, $M$ - the number of elements in $v$, and $v_1$, $v_2$, $\dots$, $v_M$ - the $M$ given numbers, we are asked to:
1. Determine the number of first-degree equations;
2. Determine the number of the $N$ equations that have at least one solution whose absolute value is in the array $v$.

# Input data

The first line of the input file `ecuatii.in` contains the number $C$, which can be $1$ or $2$, and represents the task that needs to be solved. The second line contains $N$, then on the following $N$ lines there is one equation per line, followed by the line $N+3$ which contains $M$ and on the following line, separated by spaces, the numbers: $v_1$, $v_2$, $\dots$, $v_M$.

# Output data

If $C$ is $1$, the output file `ecuatii.out` will contain the number from task $1$, that is, the number of first-degree equations. If $C$ is $2$, the output file `ecuatii.out` will contain the number from task $2$, that is, the number of equations out of the $N$ that have at least one solution whose absolute value is in the array $v$.

# Constraints and clarifications

* $1 \leq N, M \leq 100 \ 000$;
* $1 \leq v_i \leq 1 \ 000 \ 000$, $i = 1, 2, \dots, M$;
* The coefficients of the equations: $A$, $B$, $C$, $D$, $E$ are non-zero natural numbers $\leq 1 \ 000 \ 000$.
* The absolute value of $x$ is $|x|$.
* Correctly solving task $1$ will be awarded $20$ points.
* Correctly solving task $2$ will be awarded $80$ points.

# Example 1

`ecuatii.in`
```
1
3
1x^2+1x+2=0
20x+40=0
2x^2+4x+2=0
4
1 8 2 10
```

`ecuatii.out`
```
1
```

## Explanation

For this example, there is only one first-degree equation.

# Example 2

`ecuatii.in`
```
2
3
1x^2+1x+2=0
20x+40=0
1x^2+5x+6=0
4
8 1 2 10
```

`ecuatii.out`
```
2
```

## Explanation

In this example: the first equation has no real roots, the second has the root $-2$, $|-2| = 2$, which is in $v$, and the third equation has the roots $-2$, $-3$ with $|-2| = 2$ which is in $v$. Thus, there are two equations with roots that have an absolute value in $v$.