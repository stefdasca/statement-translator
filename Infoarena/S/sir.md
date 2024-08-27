# Sequence

While exploring the archaeological cave of Altamira, Professor Richard found a sequence of numbers with length $N$.

## Task

Wanting to decipher the meaning of this sequence, he needs to find the maximum length subarray with a length between $X$ and $Y$ that has the property: $MAX - MIN \leq Z$ where $MAX$ represents the maximum value in the subarray, $MIN$ the minimum value in the subarray, and $Z$ a given natural number. Help Professor Richard decipher the ancient language from the Altamira cave and thus become famous.

## Input data:

The first line of the file `sir.in` will contain 4 numbers $N$ $X$ $Y$ $Z$. The second line of the input file will contain $N$ numbers, representing the values of the sequence.

## Output data:

The first line of the file `sir.out` will print 3 numbers separated by spaces representing the maximum length of the subarray with the given property, the starting position of the subarray, and the ending position of the subarray. If there is no solution, a single number, $-1$, will be printed.

## Constraints and clarifications

$3 \leq N \leq 100 000$

$1 \leq X$

$X \leq Y$

$Y \leq N$

$0 \leq Z \leq 30 000$

The values of the sequence are natural numbers $\leq 30 000$

If there are multiple solutions, the subarray with the maximum starting position will be printed.

## Examples:

`sir.in` 
```
6 2 4 3
1 5 3 2 5 9
```

`sir.out`
```
4 2 5
```

`sir.in`
```
4 2 5 3
2 3 1 2
```

`sir.out`
```
-1
```

## Explanations

: In the first example, the maximum subarray with a length between 2 and 4 that satisfies the property given in the statement has a length of 4. This subarray starts at position 2 and ends at position 5. In the second example, there is no subarray with a length between 2 and 3 that meets the property given in the statement.