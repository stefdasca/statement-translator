## Sets

Let $M$ be a set of integers and $X$ an integer. A generally incorrect algorithm to determine a subset of $M$ that sums to $X$ is the following:
1. If $X$ is 0, the algorithm has succeeded.
2. Otherwise, find the largest element $Y$ in $M$ such that $Y$ is less than or equal to $X$. If this number does not exist, the algorithm fails (since $X$ is non-zero). If this number exists, update $X$ to $X - Y$ and repeat step 1.

We call the number $X$ lucky relative to the set $M$ if the above algorithm successfully terminates for $X$ and $M$. Given a set $A$ of $N$ elements and a number $V$ and randomly choosing a subset $B$ with uniform probability, how many numbers in the interval $[1, V]$ are lucky on average relative to the subset $B$?

## Input data

The input file `sets.in` will contain the number of tests $T$ on its first line. Next, $T$ tests follow, each having the following structure:
The first line contains the numbers $N$ and $V$, as described above.
The second line contains $N$ integers representing the set $A$.

## Output data

The output file `sets.out` will contain $T$ lines, each containing a real value, the answer for each test case.

## Constraints

$1 \leq T \leq 20$

$1 \leq N \leq 1000$

$1 \leq A[i] \leq 1000$

$1 \leq V \leq 10^9$

The output value is considered correct if its relative error is less than or equal to $10^{-6}$.

## Example

`sets.in`

```
2
2 3
1 2
5 16
1 2 3 4 6
```

`sets.out`

```
1.7500000000
11.5000000000
```

## Explanation

In the first example, we have the following four subsets that can be chosen, each with 25% probability:
1. $\{\}$ In this case, the algorithm fails for any integer.
2. $\{1\}$ In this case, 1, 2, 3 are lucky numbers.
3. $\{2\}$ In this case, 2 is a lucky number.
4. $\{1, 2\}$ In this case, 1, 2, 3 are all lucky numbers.

Thus, the answer is $0.25 \times (0 + 3 + 1 + 3) = 1.75$.