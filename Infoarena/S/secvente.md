## Task

Farfurel just got into trouble. To avoid failing in computer science, his teacher gives him 3 sequences of natural numbers with sizes $N_1$, $N_2$, $N_3$. His task is to find, for each sequence, the length of the longest subsequence with the property that the sum of its elements is divisible by 3. Farfurel does not know how to solve the problem, so his only hope is you.

## Input data

The first line contains $N_1$, the size of the first sequence. The next $N_1$ lines contain sequence 1. The $N_1 + 2$ line contains $N_2$, the size of the second sequence. The next $N_2$ lines contain sequence 2. The $N_1 + N_2 + 3$ line contains $N_3$, the size of the third sequence, and the next $N_3$ lines contain sequence 3.

## Output data

The first line contains the task for the first sequence, the second line contains the task for the second sequence, and the third line contains the task for the third sequence.

## Constraints and clarifications

$0 \leq N_1$

$N_2$

$N_3 \leq 50\ 001$

The elements of the sequences are natural numbers from the interval $[0, 500\ 000]$.

## Example

```   
secvente.in
3
3
3
3
4
4
4
3
5
5
5
```

```   
secvente.out
3
3
3
```