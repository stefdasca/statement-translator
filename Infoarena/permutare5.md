# Permutation5

Given a permutation $P$ of length $N$. We consider the operation of swapping values at two consecutive positions. We define a permutation of length $N$ as an array that contains all numbers from $0$ to $N - 1$ exactly once. Let $P = (p_0, p_1, \dots, p_i, p_{i+1}, \dots, p_{N-1})$ be a permutation and let $0 \leq i < N - 1$ be an index. After swapping the values at positions $i$ and $i+1$ in $P$, the permutation becomes $(p_0, p_1, \dots, p_{i+1}, p_i, \dots, p_{N-1})$. As a competitor (i.e., you), you can purchase such swaps. Once purchased, a swap can be used any number of times. We define the cost of $P$ as the minimum number of such swaps that need to be purchased so that the permutation can be sorted using only the purchased swaps, each used any number of times. The committee (i.e., us) changes the permutation $P$ $Q$ times by swapping the values at two arbitrary positions, not necessarily consecutive. Once a change is made to the permutation, it remains valid. For both the initial permutation and the permutations obtained after each of the committee's changes, the cost of $P$ is required.

## Input data

The input file `permutare5.in` contains, on the first line, the number $N$ of elements in the permutation under consideration, and the number $Q$ of operations. The second line contains the $N$ elements of the permutation $P$. The next $Q$ lines are of the form $a$ $b$, each representing a swap of the elements at positions $a$ and $b$.

## Output data

The output file `permutare5.out` will contain $Q + 1$ lines, containing the cost of the initial permutation, as well as the costs of all the permutations obtained after each of the committee's changes, in order.

## Constraints

$2 \leq N \leq 100\ 000$

$1 \leq Q \leq 200\ 000$

For $6$ points,

$1 \leq N \leq 1\ 000$,

$1 \leq Q \leq 10$

For $13$ points,

$2 \leq N \leq 100\ 000$,

$1 \leq Q \leq 100$

For $46$ points,

$2 \leq N \leq 50\ 000$,

$1 \leq Q \leq 50\ 000$

For $22$ points,

$2 \leq N \leq 100\ 000$,

$1 \leq Q \leq 200\ 000$ and the committee's changes swap only values at adjacent positions. More precisely, $y = x + 1$ for all the committee's changes.

## Examples

`permutare5.in`
```
3 4 
0 1 2 
0 1 
0 1 
0 2 
1 2
```

`permutare5.out`
```
0 
1 
0 
2 
2
```

`permutare5.in`
```
4 6 
0 3 2 1 
1 2 
1 3 
0 2 
0 1 
1 2 
2 3
```

`permutare5.out`
```
3 
2 
2 
4 
3 
2 
3
```

## Explanation for the first example:

In the initial permutation, $(0, 1, 2)$, no swaps are needed to sort the permutation. In the permutation after the first change, $(1, 0, 2)$, it is necessary to purchase the swap $(0, 1)$. The permutation after the second change is identical to the initial one. The penultimate permutation is $(2, 0, 1)$, and it is necessary to purchase the swaps $(0, 1)$ and $(1, 2)$. The final permutation is $(2, 1, 0)$, and both swaps $(0, 1)$ and $(1, 2)$ remain necessary *(even if they are used multiple times, each is purchased only once)*.