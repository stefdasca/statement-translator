# Magic Sequence

Lately, on the planet Miada, the so-called magic sequences have become trendy. We say that a sequence $V$ is magic if it can be constructed from operations of the type:

- Add element $X$ to the sequence. This operation is allowed only if the sequence is empty.
- Add element $X$ to the sequence, on top of the element at position $pos$:
  1. If $V[pos]$ is less than $X$, then all elements in the sequence $V$ starting from position $pos + 1$ will move one position to the right, and $X$ will be placed at position $pos + 1$.
  2. If $V[pos]$ is greater than $X$, then all elements in the sequence $V$ starting from position $pos$ will move one position to the right, and $X$ will be placed at position $pos$.

Given $T$ sequences, determine for each sequence whether it is a magic sequence or not.

## Input data

The input file `magicsequence.in` contains:
- The first line contains $T$, representing the number of tests.
- For each test, the first line contains a natural number $N$, representing the length of the sequence, and the second line contains $N$ distinct natural numbers, representing the numbers in the sequence.

## Output data

The output file `magicsequence.out` will contain $T$ lines. On line $i$ will be the answer for test $i$: \texttt{YES} if the sequence is magic, and respectively \texttt{NO} if it is not.

## Constraints and clarifications

$$1 \leq T \leq 20$$

$$1 \leq N \leq 20000$$

$$1 \leq V[i] \leq 10^9$$ 

The numbers are distinct two by two.

## Example

`magicsequence.in`
```
2
3
2 1 3
2
2 1
```

`magicsequence.out`
```
YES
NO
```

## Explanation

For the first example, we can obtain the sequence as follows:
1. Add $2$ to the sequence.
2. Add $3$ to the sequence, on top of $2$. The sequence becomes $2 \ 3$.
3. Add $1$ to the sequence, on top of $3$. The sequence becomes $2 \ 1 \ 3$.