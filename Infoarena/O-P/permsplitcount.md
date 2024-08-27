Permsplitcount

The Romanian Commission favors problems that are easy to prepare rather than those with beautiful solutions. Thus, unlike the Russian or Polish Commissions, the focus is on problems that do not need verification or can have a random generator, rather than a beautifully crafted problem without rotations. Excerpt from "Testimony from the Commission's Work" by Ion Luca Caragiale. Indeed, Caragiale remains ever relevant. However, what Caragiale does not mention here is that it's not so easy to evaluate how good random tests are. In this problem, we ask you to decide if we could have safely generated random tests for the Permsplit problem. More precisely, we would like to know for a given $N$ how many permutations of length $N$ have a solution of $-1$ in the context of the PermSplit problem.

## Input data

The input file `permsplitcount.in` will contain a single line with two values: $N$ and $MOD$.

## Output data

The output file `permsplitcount.out` will contain a single value, the answer to the problem modulo $MOD$.

## Constraints

$1 \leq N \leq 1\ 500$

$2 \leq MOD \leq 1\ 000\ 000\ 000$

## Example

`permsplitcount.in`:
```
5 13
```

`permsplitcount.out`:
```
4
```

## Explanation

The number of solutions is $30 \mod 13 = 4$. Among the 30 counted permutations is, for example, the permutation $5\ 2\ 4\ 1\ 3$.