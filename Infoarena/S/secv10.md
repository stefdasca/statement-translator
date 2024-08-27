# Secv10

Given 3 strings $S$, $st$, and $dr$. How many subarrays from $S$ have the prefix $st$ and the suffix $dr$? 

## Input data

The input file `secv10.in` contains on the first line the number $T$ representing the number of tests. For each test, the first line contains the string $S$, the second line contains the string $st$, and the last line contains the string $dr$. 

## Output data

The output file `secv10.out` will contain $T$ lines, each line $i$ containing the answer for test $i$. 

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq |S| \leq 100\,000$

$1 \leq |st| \leq 100\,000$

$1 \leq |dr| \leq 100\,000$

The strings contain only lowercase English letters. 

## Example

`secv10.in`
```
2
abababb
a
b
abababb
a
ab
```

`secv10.out`
```
9
6
```