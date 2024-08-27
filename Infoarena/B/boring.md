Boring

You are still in the algorithms lab. The lab assistant has recovered a bit. He takes off his sunglasses and says: We say that a string $A$ is a $K$-repetition if there exists a string $B$ such that $A = B + B + B + \dots$ (a total of $K$ times), where $+$ denotes the concatenation operation. For example, "dada" is a $2$-repetition, and $andreiandreiandrei$ is a $3$-repetition. Given a string $S$, you need to find out how many of its subarrays are $K$-repetitions, for all $K$ from $1$ to $|S|$.

## Input data

The input file `boring.in` will contain on its first line the value $T$, representing the number of tests in the file. The next $T$ lines contain each a string, representing the string $S$.

## Output data

The output file `boring.out` will contain $T$ lines. Each line will contain $|S|$ values, the $a_i$-th of these representing the number of subarrays of the string $S$ that are $i$-repetitions.

## Constraints and clarifications

$1 \leq T \leq 1000$

$1 \leq |S| \leq 300\ 000$

The sum of the values of $|S|$ in the same input file is at most equal to $300\ 000$.

$S$ contains only lowercase English letters.

A subarray of a string is a subsequence of consecutive elements of it.

## Example

`boring.in`
```
2
aaaaa
barbaraa
```

`boring.out`
```
15 6 3 2 1
36 2 0 0 0 0 0 0
```

## Explanation

Note that, generally, all subarrays of $S$ are $1$-repetitions.