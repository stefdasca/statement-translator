## Task

You are given the following algorithm for sorting the elements of an array of $N$ natural numbers in ascending order:

$$
\begin{align*}
ok &= 1; \\
\text{while}(ok) \{ \\
\ \ \ ok &= 0; \\
\ \ \ \text{for}(i = 1; i < N; i++) \{ \\
\ \ \ \ \ \ \ \text{if}(v[i] > v[i + 1]) \{ \\
\ \ \ \ \ \ \ \ \ \ aux = v[i]; \\
\ \ \ \ \ \ \ \ \ \ v[i] = v[i + 1]; \\
\ \ \ \ \ \ \ \ \ \ v[i + 1] = aux; \\
\ \ \ \ \ \ \ \ \ \ ok = 1; \\
\ \ \ \ \ \ \ \} \\
\ \ \ \} \\
\}
\end{align*}
$$

More precisely, as long as the array $v$ is not sorted, we will take any 2 values located at consecutive positions, and if the larger element appears before the smaller one, we will swap the values. Tapescu received a permutation of $N$ elements (a sequence of $N$ distinct natural numbers from the interval $[1,N]$). He started sorting the elements of the permutation using the above algorithm. Bored and in a hurry to play on Tinder, he decided to stop after the first $K$ swaps of the algorithm. Now Tapescu makes an offer: he will give you the permutation of length $N$ and the value $K$, and you have to tell him what the permutation will look like after the first $K$ swaps. If you do this, he will give you 100 points and possibly 5 euros.

## Input data

The input file `kbubblesort.in` contains on the first line 2 natural numbers $N$ and $K$. The second line contains $N$ distinct natural numbers from the interval $[1,N]$ representing the permutation of length $N$.

## Output data

The output file `kbubblesort.out` contains on the first line $N$ natural numbers representing how the permutation will look after the first $K$ swaps of the BubbleSort algorithm (the above algorithm).

## Constraints and clarifications

$$1 \leq N \leq 1\ 000\ 000$$

$$1 \leq K \leq 100\ 000\ 000$$

It is guaranteed that after the first $K$ swaps, the permutation will not be sorted.

## Example

`kbubblesort.in`

```
5 4
4 2 5 1 3
```

`kbubblesort.out`

```
2 1 4 3 5
```