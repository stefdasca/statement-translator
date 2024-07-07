
We will call a PM sequence a succession consisting of plus and minus, which does not contain two adjacent minus signs.
For example, there are $5$ PM sequences of length $3$: +++, ++-, +-+, -++, -+-.

# Input data

The input file `pm.in` contains on the first line two natural numbers separated by a space $x \\ y$, with the meaning from the statement.

# Output data

The output file `pm.out` will contain a single line, which will contain a single natural number, representing the number of PM sequences that contain $x$ plus signs and $y$ minus signs.

# Constraints and clarifications

* $0 \\leq y \\leq x \\leq 250$
* The result will have a maximum of $100$ digits.
* For $50\\%$ of the evaluation tests $x \\lt 32$.

# Example 1

`pm.in`
```
2 1
```

`pm.out`
```
3
```
# Example 2

`pm.in`
```
4 2
```

`pm.out`
```
10
```
