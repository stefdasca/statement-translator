An interesting property of irreducible fractions is that any fraction can be obtained by the following rules:

* On the first level is the fraction $\frac{1}{1}$;
* On the second level, to the left of the fraction $\frac{1}{1}$ on the first level, we place the fraction $\frac{1}{2}$, and to its right, the fraction $\frac{2}{1}$;

$$
\def\arraystretch{1.5}
\begin{array}{c:c:c:c}
\text{level 1:}& & \frac{1}{1} & \\ \hline
\text{level 2:}& \frac{1}{2} & & \frac{2}{1} \\
\hdashline
\end{array}
$$

* On each level $k$, under each fraction $\frac{i}{j}$ from the above level, place the fraction $\frac{i}{(i+j)}$ on the left, and the fraction $\frac{(i+j)}{i}$ on the right.

$$
\def\arraystretch{1.5}
\begin{array}{c:c:c:c:c:c}
\text{level 1:}& & & \frac{1}{1} \\ \hline
\text{level 2:}& & \frac{1}{2} & & \frac{2}{1}\\ \hline
\text{level 3:}& \frac{1}{3} & & \frac{3}{2} \ \ \ \ \frac{2}{3} & & \frac{3}{1} \\
\hdashline
\end{array}
$$

# Task

Given any fraction by its numerator and denominator, determine the level number on which the fraction (or an equivalent fraction with the same value) is found.

# Input data

Input file: `fractii.in`

* Line $1$: $N$, $M$, two non-zero natural numbers separated by a space, representing the numerator and the denominator of a fraction (numerator and denominator, respectively).

# Output data

Output file: `fractii.out`

* Line $1$: $niv$, a non-zero natural number, representing the level number corresponding to the fraction.

# Constraints and clarifications

* $1 < N, M \leq 2 \ 000 \ 000 \ 000$ (two billion)

# Example 1

`fractii.in`
```
13 8
```

`fractii.out`
```
6
```

# Example 2

`fractii.in`
```
12 8
```

`fractii.out`
```
3
```
