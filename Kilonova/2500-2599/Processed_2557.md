```markdown
A superstring is an infinite sequence formed by non-zero natural numbers written without spaces between them, starting with $1$: $1223334444\dots1010\dots$ (each number $x$ appears exactly $x$ times).

# Task
Answer $T$ queries of the form: What digit is in the superstring at position $k$?

# Input data
The input file `superstring.in` contains on the first line the number of tests $T$. The following $T$ lines contain a single natural number $k$, corresponding to the current query.

# Output data
The output file `superstring.out` contains $T$ lines, each line $i$ containing the answer to the $i$-th query from the input file.

# Constraints and clarifications
- $1 \leq T \leq 31\ 000$
- $1 \leq k \leq 10^{15}$
- The positions of the digits in the superstring are numbered starting with 1
- For 15% of the tests $T$, $k \leq 5\ 000$
- For another 35% of the tests $k \leq 10^{6}$

# Example
`superstring.in`
```
4
1
3
46
47
```
`superstring.out`
```
1
2
1
0
```
```