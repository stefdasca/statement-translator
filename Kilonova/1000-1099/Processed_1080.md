Sure, here is the translated text:

---

A range of natural numbers can be one of the well-known mathematical ranges:
* `(a, b)` $= \\{x \\ \\text{natural}; a < x < b\\}$
* `(a, b]` $= \\{x \\ \\text{natural}; a < x \\leq b\\}$
* `[a, b)` $= \\{x \\ \\text{natural}; a \\leq x < b\\}$
* `[a, b]` $= \\{x \\ \\text{natural}; a \\leq x \\leq b\\}$

A set of natural numbers can be described as an expression formed by one or more ranges, with an allowed operation between any two ranges located at consecutive positions. The allowed operations are:
* *Intersection* – denoted by the letter $n$
* *Union* – denoted by the letter $u$
* *Difference* – denoted by the character $\text{–}$ (minus).

Intersection has the highest priority. Union and difference have the same priority, lower than the priority of intersection. To evaluate an expression, operations are performed in decreasing order of priority; operations with the same priority are evaluated from left to right.
For example, the expression `[7,10)u(1,4)n[2,6)-(3,8) = [7,10)u[2,3]-(3,8)` has as its value a set of integer numbers, so {$x$ integer; $2 \\leq x \\leq 3$ or $8 \\leq x \\leq 9$} = $\\{2,3,8,9\\}$.

Given a sequence of queries, each query containing a number and an expression, determine the answer for each query (`DA` if the given number belongs to the set resulting from the evaluation of the expression, otherwise `NU`).

# Task

The input file `opmult.in` contains on the first line the natural number $T$ which represents the number of queries. Each of the following $T$ lines contains a natural number $y$, followed by a space, then by an expression in the form described in the statement, representing a query.

# Input data

The output file `opmult.out` will contain $T$ lines, one line for each of the $T$ queries. Line $i$ will contain the word `DA` if for the $i$-th query from the input file the number $y$ belongs to the set resulting from the evaluation of the expression in the query, otherwise the word `NU`.

# Output data

# Constraints and clarifications

* $1 \\leq T \\leq 10$
* The endpoints of the intervals, as well as the numbers in the queries, are natural numbers in the range `[1,255]`.
* The length of an expression in the input file is a maximum of $2 \\ 000$ characters.
* The expressions do not contain spaces.
* Each line in the input and output files ends with a newline character.

# Example

`opmult.in`
```
2
6 [2,6]n[6,20]
4 (1,4)n[2,6)u[7,10)-(3,8)
```

`opmult.out`
```
DA
NU
```

## Explanation

There are $T=2$ queries.
`[2,6]n[6,20]` = `[6,6]` = $\\{6\\}$, so the answer is $DA$.
`(1,4)n[2,6)u[7,10)-(3,8)` = `[2,3]u[7,10)-(3,8)` = $\\{2,3,7,8,9\\} - \\{4,5,6,7\\} = \\{2,3,8,9\\}$, so the answer is $NU$.

---

Please let me know if you need any further assistance!