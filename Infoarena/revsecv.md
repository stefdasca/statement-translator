## Task

Given a string $A$ of the form $a_0 a_1 a_2 \dots a_{n-1}$. The **inverse** of the string $A$ is defined as $\mathrm{Inv}(A) = a_{n-1} a_{n-2} \dots a_1 a_0$, meaning the string formed by writing the characters of $A$ in reverse order. How many triplets $i, j, k$ with $0 \leq i \leq i + k - 1 \leq n - 1$, $i + k \leq j \leq j + k - 1 \leq n - 1$ exist such that $a_i a_{i+1} a_{i+2} \dots a_{i+k-1} = \mathrm{Inv}(a_j a_{j+1} a_{j+2} \dots a_{j+k-1})$. In other words, how many pairs of disjoint subarrays of equal length in $A$ have the property that the second one is the inverse of the first one?

## Input data

The input file `revsecv.in` will contain the string $A$ on its only line.

## Output data

The output file `revsecv.out` will contain a single natural number, the answer to the question.

## Constraints and clarifications

$1 \leq |A| \leq 100\ 000$

For tests worth 20 points $|A| \leq 200$

For tests worth 40 points $|A| \leq 5\ 000$

Characters of $A$ are lowercase letters of the English alphabet.

## Example

`revsecv.in`
```
rabaczeabaca
```

`revsecv.out`
```
16
```