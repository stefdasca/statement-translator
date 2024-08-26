## Task 

KL3.14 received a very important task. He must solve $N$ hacks in the order they appear. A hack can be solved in 2 ways: Option $A$ in which hack $i$ can be solved in time $a_i$ Option $B$ in which hack $i$ can be solved in time $b_i$ KL3.14 needs to solve the hacks in minimal time, but there's a problem. He found out that if he solves a hack using option $A$, then all hacks from $i+1$ to $N$ will be resolved twice as slowly. Specifically, the time to solve a hack will be doubled. Since KL3.14 just learned that he needs to upgrade to another level and no longer has time to solve the hacks, he asks you to solve them in minimal time.

## Input data 

The input file `hacker3.in` contains a number $N$ representing the number of hacks that need to be solved. The next $N$ lines contain 2 natural numbers $a_i$ and $b_i$. The hacks must be solved in order from hack 1 to hack $N$.

## Output data 

The output file `hacker3.out` will contain a single number representing the minimum time to solve all $N$ hacks.

## Constraints and clarifications 

$1 \leq N \leq 100\ 000$

$1 \leq a_i \leq 2\ 000\ 000\ 000$

$1 \leq b_i \leq 2\ 000\ 000\ 000$

for 10% of the tests $N \leq 15$

for another 10% of the tests $N \leq 100$

for another 20% of the tests $N \leq 1000$

for another 30% of the tests $N \leq 10\ 000$

## Example 

`hacker3.in`
```plaintext
2
1 4
3 1
```

`hacker3.out`
```plaintext
3
```