## Task

Given a natural number $N$ and a sequence of $N$ natural numbers: $A_1$, $A_2$, $\dots$, $A_N$. We define $C(X, P, B) = the\ number\ of\ occurrences\ of\ P\ as\ a\ subsequence\ in\ the\ representation\ in\ base\ B\ of\ X$. Answer $Q$ questions like this: Given a base $B$ and a sequence $P$, written in base $B$, calculate and print the sum of $C(Ai, P, B) * Ai$. Note! The sequence $P$ can start with the digit 0 (zero).

## Input data

The input file `basequery.in` contains, on the first line, the natural number $N$. The second line contains $N$ natural numbers, $A_1$, $A_2$, $\dots$, $A_N$, the elements of the sequence. The third line contains the number $Q$. Each of the following $Q$ lines contains a natural number $B$ and a sequence of digits in base $B$, defined as $P$ in the statement.

## Output data

The output file `basequery.out` will contain $Q$ lines. Each line $i$ will contain a single natural number representing the answer for question $i$.

## Constraints and clarifications

$1 \leq N \leq 40000$

$1 \leq Q \leq 100000$

$1 \leq Ai \leq 2000000000$, where $1 \leq i \leq N$

$2 \leq B \leq 16$

$1 \leq P (10) < 1024$, where $P (10)$ is the value represented by the sequence $P$ in base $B$, converted to base 10.

$P$ can start with the digit 0 (zero).

The sequence $P$ is no more than 40 characters long.

## Example

`basequery.in`

```
5
85 82 5 5515515 243
3
2 01
10 5
16 F3
```

`basequery.out`

```
33093757
27577665
243
```

## Explanation

For the first query, we have $B = 2$ and $P = 01$. Converting the numbers in the array to base 2, we have:

$85 (10) = 1010101 (2)$ - Sequence $01$ appears 3 times

$82 (10) = 1010010 (2)$ - Sequence $01$ appears 2 times

$5 (10) = 101 (2)$ - Sequence $01$ appears 1 time

$5515515 (10) = 10101000010100011111011 (2)$ - Sequence $01$ appears 6 times

$243 (10) = 11110011 (2)$ - Sequence $01$ appears 1 time

In conclusion, the answer is:

$3 * 85 + 2 * 82 + 1 * 5 + 6 * 5515515 + 1 * 243 = 33093757$.