It is considered the following data structure:

~[numinum.png]

* At the top of the structure is the fraction $\displaystyle \frac{1}{1}$.
* From each vertex where the fraction $\displaystyle \frac{p}{q}$ is found, two more fractions are formed by drawing 2 line segments as follows: to the left the fraction $\displaystyle \frac{p}{p+q}$ and to the right the fraction $\displaystyle \frac{p+q}{q}$.

# Task

Given the numerator and the denominator of **two different irreducible fractions** in the structure, determine the **minimum number** of line segments required to connect the two fractions in the given structure.

# Input data

The first line of the input file `numinum.in` contains a natural number $N$. Each of the following $N$ lines contains $4$ natural numbers $x_i$, $y_i$, $a_i$, $b_i$, separated by a space where $x_i$, $y_i$ represent the numerator and the denominator of the first fraction on line $i+1$, and $a_i$, $b_i$ represent the numerator and the denominator of the second fraction on line $i+1$.

# Output data

The output file `numinum.out` will contain $N$ lines. Each line $i$ will contain the minimum number of line segments required to connect, in the given structure, the fraction $\displaystyle \frac{x_i}{y_i}$ with the fraction $\displaystyle \frac{a_i}{b_i}$.

# Constraints and clarifications

* $1 \leq N \leq 10\, 000$;
* $1 \leq x_i, y_i, a_i, b_i \leq 10^9$;

# Example

`numinum.in`
```
1
4 3 2 5
```

`numinum.out`
```
6
```

## Explanation

$N = 1$, $x_1 = 4$, $y_1 = 3$, $a_1 = 2$, $b_1 = 5$.

To connect the fraction $\frac{4}{3}$ with the fraction $\frac{2}{5}$, we need at least $6$ segments, as follows:

$\frac{4}{3} \rightarrow \frac{1}{3} \rightarrow \frac{1}{2} \rightarrow \frac{1}{1} \rightarrow \frac{2}{1} \rightarrow \frac{2}{3} \rightarrow \frac{2}{5}$