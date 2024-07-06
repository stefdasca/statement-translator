Given a sequence of $n$ lowercase letters, where the letter `a` is assigned the value $1$, the letter `b` the value $2$, $\dots$, the letter `z` the value $26$. One can perform operations of the type: change a letter $c_1$ to letter $c_2$ with a cost of $c_1+c_2$.

# Task

Determine the minimum total cost of operations needed to make the sequence increase.

# Input data

The input file `nondecreasing.in` will contain on the first line the sequence of lowercase letters without spaces.

# Output data

The output file `nondecreasing.out` will contain a single natural number that represents the minimum total cost of all operations that lead to an increasing sequence.

# Constraints and clarifications

* The length of the sequence is between $3$ and $50\ 000$.

# Example

`nondecreasing.in`
```
dbca
```

`nondecreasing.out`
```
9
```

## Explanation

Change `d` to `a` with a cost of $d+a=4+1=5$, then change the last `a` to `c` with a cost of $a+c=1+3=4$. The resulting increasing sequence is `abcc` with a total cost of $5+4=9$.