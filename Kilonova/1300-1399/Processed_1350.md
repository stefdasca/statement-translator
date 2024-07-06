```markdown
It is considered that there are $3$ arrays, named $A, B$ and $val$, each having $N$ non-zero natural elements. The elements of the arrays are indexed from $1$ to $N$. Knowing $A[1]$, $B[1]$ and a non-zero natural value $P$, the rule to calculate the elements of the arrays is as follows:

For $2 \leq i \leq N$ we have:

$$A[i] = ((A[i-1] + P - 1) \ \textit{\textbf{XOR}} \ (B[i-1] + 1) \ \textit{\textbf{mod}} \ P$$

$$B[i] = ((A[i-1] + P - 1) \ \textit{\textbf{OR}} \ (B[i-1] + 1) \ \textit{\textbf{mod}} \ P$$

For $1 \leq i \leq N$ we have:

$$val[i] = \max \{ 1, ((i \ \textit{\textbf{mod}} \ P) \ \textit{\textbf{XOR}} \ ((A[i] + 1) \ \textit{\textbf{AND}} \ (B[i] + 1)) \ \textit{\textbf{mod}} \ P))  \ \textit{\textbf{mod}} \ P \}$$

The operations used in the above formulas have the following meaning:

* $\textit{\textbf{XOR}}$ : bitwise XOR
* $\textit{\textbf{OR}}$ : bitwise OR
* $\textit{\textbf{AND}}$ : bitwise AND
* $F \textit{\textbf{mod}} G$ : represents the remainder of dividing $F$ by $G$

We define $Prod[i]$ as being equal to: (the product of all elements of the array val, except $val[i]$) $\textit{\textbf{mod}} Q$.

More specifically, $$Prod[i] = (val[1] \cdot val[2] \cdot \ldots \cdot val[i-1] \cdot val[i+1] \cdot \ldots \cdot val[N]) \ \textit{\textbf{mod}} \ Q$$.

# Task

Compute the value $Rez = Prod[1] \ \textit{\textbf{XOR}} \ Prod[2] \ \textit{\textbf{XOR}} \ \ldots \ \textit{\textbf{XOR}} \ Prod[N]$ (i.e., $\textit{\textbf{XOR}}$ between all $N$ values $Prod[i]$, $1 \leq i \leq N$).

# Input data

The input file `xp.in` contains, on the first (and only) line, $5$ natural numbers separated by a space, representing, in order, the values $N, A[1], B[1], P$ and $Q$.

# Output data

The output file `xp.out` will contain the value $Rez$.

# Constraints and clarifications

* $1 \leq N \leq 4 \ 000 \ 000$
* $2 \leq P \leq 1 \ 000 \ 000 \ 000$
* $2 \leq Q \leq 1 \ 000 \ 000 \ 000$
* $0 \leq A[1], B[1] \leq P - 1$
* For $30\%$ of the tests we will have $N \leq  10 \ 000$
* For another $20\%$ of the tests we will have $10 \ 001 \leq N \leq 200 \ 000$
* The problem does not pursue finding any special property of the generation relationships of the arrays $A, B$ and $val$

# Example 1

`xp.in`
```
5 4 6 10 15
```

`xp.out`
```
10
```

# Explanation

We obtain the following arrays $A, B$ and $val$:

$A[1]=4, B[1]=6, val[1]=4 \\
A[2]=0, B[2]=5, val[2]=2 \\
A[3]=5, B[3]=5, val[3]=5 \\
A[4]=8, B[4]=4, val[4]=5 \\
A[5]=0, B[5]=1, val[5]=5$

We obtain the following values for the array $Prod$ (in order, from $1$ to $5$):
$10, 5, 5, 5, 5$.

We get $Rez = 10 \ \textit{\textbf{XOR}} \ 5 \ \textit{\textbf{XOR}} \ 5 \ \textit{\textbf{XOR}} \ 5 \ \textit{\textbf{XOR}} \ 5 = 10$.

# Example 2

`xp.in`
```
3999999 9003 3333 30000 900330000
```

`xp.out`
```
594979072
```
```