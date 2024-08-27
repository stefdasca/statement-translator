# Frequent

## Task

An astrobiologist is studying life on the planet Alphabet. On this planet, the genetic material of life has $26$ nucleotides. Therefore, the genome of any living creature on the planet can be represented as a string of lowercase letters from the Latin alphabet. The astrobiologist has determined the DNA of $K$ life forms, not necessarily distinct, with a total length of $N$ nucleotides. Now, she wants to find DNA subarrays that frequently appear in the genetic code of these life forms. Let $L(i)$ be the longest subarray of consecutive nucleotides that appears in at least $i$ of the life forms, for $2 \leq i \leq K$. Note that $L(i)$ can even be $0$. Your task is to help the astrobiologist compute the sequence $L$.

## Input data

The input file `frequent.in` contains an integer $K$ on the first line, representing the number of life forms. Each of the next $K$ lines contains a non-empty string of lowercase letters from the Latin alphabet, the string with index $i$ representing the genetic code of being $i$. Each string is followed by a newline character.

## Output data

The output file `frequent.out` will contain $K - 1$ lines, representing the values $L(2), L(3), \dots, L(K)$, one on each line.

## Constraints and clarifications

$2 \leq N \leq 200\ 000$

$2 \leq K \leq N$

## Subtasks

The tests will be scored individually.

Subtask $1$ ($30\%$): $N \leq 10\ 000$

Subtask $2$ ($40\%$): $N \leq 100\ 000$

Subtask $3$ ($30\%$): Initial limits.

## Example

`frequent.in`

```
6
matter
animate
pattern
thermal
domain
teammate
```

`frequent.out`

```
5
3
2
2
1
```

## Explanation

- $atter$ appears in two of the strings.
- $mat$ appears in three of the strings.
- $ma$ (or $at$ or $te$) appear in four of the strings.
- $ma$ appears in five of the strings.
- $a$ appears in all the strings.