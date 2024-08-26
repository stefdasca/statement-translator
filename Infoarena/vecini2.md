# Neighbors2

Mihai is a well-behaved child with a new preference. He has to solve a problem involving two strings $a$ and $b$ of length $N$ that contain only lowercase letters of the English alphabet. Mihai wants to change the order of the letters in the string $b$ to obtain two other strings $b_1$ and $b_2$ of length $N$, such that $b_1$ is lexicographically smaller than $a$ and is the largest string that can be obtained by rearranging the letters of $b$, and $b_2$ is a string larger than $a$ and the smallest lexicographically that can be obtained by rearranging the letters of $b$. If no solution exists for a string, $0$ should be displayed instead.

## Task

Given two strings of letters of the same length $N$, determine the strings $b_1$ and $b_2$.

## Input data

The input file `vecini2.in` will contain on the first line a natural number $N$, and on the second line the string $a$, and on the next line the string $b$.

## Output data

On the first line of the file `vecini2.out`, the string $b_1$ will be written or $0$ if it does not exist, and on the second line the string $b_2$ will be written or $0$ if it does not exist.

## Constraints and clarifications

The length of each string will be between $5$ and $5000$ letters.

## Example

`vecini2.in`
```
9
abcabcabc
axyzbbaaa
```

`vecini2.out`
```
abbzyxaaa
abxaaabyz
```

## Explanation

$abbzyxaaa$ is the largest lexicographic string that can be obtained from $axyzbbaaa$ (smaller than $abcabcabc$).

$abxaaabyz$ is the smallest lexicographic string that can be obtained from $axyzbbaaa$ (larger than $abcabcabc$).