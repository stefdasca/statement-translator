
# Task

You are given an integer $n$. Display a number with $n$ digits in base $10$ with the property that it is composed only of the digits $0$ and $1$, and it is a multiple of $n$.

For example, if $n = 6$, $101100$ is such a number.

# Input data

The first line contains $n$, the number of digits of the sought number.

# Output data

The first line will contain a single integer of $n$ digits, representing the required answer. Any correct solution is accepted, as long as the number respects the properties mentioned above.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000\ 000$;
* For tests worth $24$ points, $n \leq 10\ 000$.

# Example

`stdin`
```
8
```

`stdout`
```
10110000
```

## Explanation

$$\frac{10110000}{8} = 1263750$$
