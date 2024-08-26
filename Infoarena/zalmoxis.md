# Zalmoxis

Tanaka has become interested in Dacian Mythology (Dacians lived in the area of Romania before the Romans). In this mythology, Zalmoxis was the supreme god, and Pleistoros was the god of war. In Tanaka's new interpretation of the mythology, Zalmoxis has a new power, ZalStrike, and he likes ZalSequences. ZalStrike is an attack that can be applied to non-negative sequences of integers. The attack consists of choosing a strictly positive integer $x$ from the sequence and replacing it with two values $x - 1$. For example: $\{1\} \rightarrow \{0, 0\}$ $\{1, 23, 3\} \rightarrow \{1, 22, 22, 3\}$ But it is not the case that $\{1, 3\} \rightarrow \{2, 1, 2\}$, because the order in the sequence matters. ZalSequences – Zalmoxis's favorite sequences – are the following: The sequence $\{30\}$. A sequence that can be obtained by applying a ZalStrike to another ZalSequence. For example, $\{29, 29\}$ and $\{29, 28, 27, 27\}$ are ZalSequences, but $\{28, 29, 28\}$ is not. Initially, Zalmoxis creates a ZalSequence of length $N + K$. Thereafter, one of his enemies destroys $K$ values from this sequence, leaving only $N$ values. Let this sequence be noted as $S$. Given $N$, $K$, and $S$, add $K$ values to $S$ in such a way that any ZalSequence of length $N + K$ is created. It is guaranteed that for any test, there is a solution.

## Input data

The first line of the input file `zalmoxis.in` contains the positive integers $N$ and $K$. The second line contains $N$ non-negative integers, the values of $S$.

## Output data

The first line of the output file `zalmoxis.out` contains the non-negative integers of the ZalSequence of length $N + K$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq K \leq 1\ 000\ 000$

$1 \leq N + K \leq 1\ 000\ 000$

The sequence in the input file is a subsequence of a ZalSequence of length $N + K$.

For tests worth $30$ points, $K = 1$.

All the tests used are not grouped.

## Example

`zalmoxis.in` 

```
5  1
29  27  25  25  28
```

`zalmoxis.out`

```
29  27  25  25  26  28
```

`zalmoxis.in` 

```
1  5
29
```

`zalmoxis.out`

```
29  29  28  27  26  25  25
```

## Explanation

In the first example, $\{29, 27, 25, 25, 26, 28\}$ can be obtained from $\{30\}$ through the following ZalStrikes: $\{30\} \rightarrow \{29, 29\} \rightarrow \{29, 28, 28\} \rightarrow \{29, 27, 27, 28\} \rightarrow \{29, 27, 26, 26, 28\} \rightarrow \{29, 27, 25, 25, 26, 28\}$

In the second example, $\{29, 28, 27, 26, 25, 25\}$ can be obtained from $\{30\}$ through the following ZalStrikes: $\{30\} \rightarrow \{29, 29\} \rightarrow \{29, 28, 28\} \rightarrow \{29, 28, 27, 27\} \rightarrow \{29, 28, 27, 26, 26\} \rightarrow \{29, 28, 27, 26, 25, 25\}$