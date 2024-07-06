A private detective has a special case to solve. It is about embezzlement. In order to solve the case, he needs to find a sequence with $n$ distinct codes. Each code is a natural number written in base $10$. Unfortunately, things are not simple because from the investigations carried out, two pieces of information have been obtained. The first piece of information is that the sum of the squares of the codes is a perfect cube, and the second says that the sum of the cubes of the codes is a perfect square.

# Task

Help the detective to find a sequence of codes $x_1, x_2, \ldots, x_n$ that satisfy the conditions in the statement and $x_i \leq n^{14}$ for any $i$ with $1 \leq i \leq n.$

# Input data

The input file `coduri.in` contains on the first line the natural number $n$.

# Output data

The output file `coduri.out` will contain $n$ lines, each one for each code in the sequence, in ascending order.

# Constraints and clarifications

* $1 \leq n \leq 20$

# Example

`coduri.in`
```
2
```

`coduri.out`
```
625
1250
```