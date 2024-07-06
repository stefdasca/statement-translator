```markdown
# Task

You are given two numbers $n$ and $k$. Find any sequence of $k$ natural numbers $x_1,x_2,\ldots,x_k$ that satisfies the following conditions:

- $x_1 < x_2 < \ldots < x_k$;
- $x_1+x_2+\ldots+x_k=n$;
- Among all sequences that satisfy the above conditions, $x_k-x_1$ is minimal.

# Input data

The first line of the input file `ksum.in` contains two natural numbers $n$ and $k$.

# Output data

The output file `ksum.out` will contain $k$ natural numbers $x_1,x_2,\ldots,x_k$ that satisfy the conditions from the statement.

# Constraints and clarifications

- $1 \le n \le 10^{18}$;
- $1 \le k \le 10^6$, $\frac{k \cdot (k+1)}{2} \le n$;
- For 10 points, $k \le 2$;
- For an additional 30 points, $n \le 10^6$;
- For an additional 30 points, $n \le 10^9$;
- For the remaining 30 points, no additional constraints are imposed.

# Example 1

`ksum.in`
```
37 5
```

`ksum.out`
```
5 6 7 9 10
```

## Explanation

$37=5+6+7+9+10$, and $10-5=5$ is the smallest possible value of $x_5-x_1$.

# Example 2

`ksum.in`
```
1000000000 1
```

`ksum.out`
```
1000000000
```

## Explanation

$10^9=10^9$

# Example 3

`ksum.in`
```
14 4
```

`ksum.out`
```
2 3 4 5
```

## Explanation

$14=2+3+4+5$
```