# Perle2

Laura received a necklace with $N$ pearls. She represented how much she likes each pearl on the necklace in an array $A$ of integers. More precisely, the value at position $i$ in the array tells us how much Laura likes the $i$-th pearl. She would like to keep a subarray of pearls from the necklace that she likes the most, but she is aware that the length of the chosen subarray affects the beauty of the necklace with a known factor $K$. Therefore, she asks you to find a subarray $[i, j]$ that maximizes the value $(A_i + A_{i+1} + \dots + A_j) - K*(j-i+1)$.

## Task

Determine the maximum possible value of a subarray from the given array. The next $N$ lines contain one integer from the array $A$.

## Input data

The input file `perle2.in` contains on the first line two integers $N$ and $K$. The next $N$ lines contain one integer representing an element of the array $A$.

## Output data

The output file `perle2.out` contains a single integer corresponding to the required value.

## Constraints

$1 \leq N \leq 100\,000$

$-10\,000 \leq K \leq 10\,000$

$-10\,000 \leq A_i \leq 10\,000$

If the maximum possible value is negative, then Laura will prefer not to choose any pearl.

For $30\%$ of the tests, $N \leq 1\,000$.

## Example

`perle2.in`

```
6 3
2
6
7
1
4
-5
```

`perle2.out`

```
7
```

## Explanation

The maximum value subarray is $[2, 3]$.