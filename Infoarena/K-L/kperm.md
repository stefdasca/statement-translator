##  Kperm

Let $N$ and $K$ be given natural numbers. A permutation with $N$ elements is called a $K$-permutation if the sum of any $K$ consecutive elements in the permutation is divisible by $K$. For example, $\{2, 4, 3, 5, 1\}$ is a $3$-permutation because $2+4+3$, $4+3+5$, and $3+5+1$ are numbers divisible by $3$. How many $K$-permutations with $N$ elements exist?

##  Input data

The first line of the input file `kperm.in` contains $N$ and $K$. 

##  Output data

The first line of the output file `kperm.out` contains the number of $K$-permutations with $N$ elements, modulo $666013$ (the remainder of the total number of permutations with the required properties modulo $666013$). 

##  Constraints and clarifications

$2 \leq K$

$K \leq N$

$N \leq 5000$

##  Example

`kperm.in
5 3`

`kperm.out
8`