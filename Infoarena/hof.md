# Hof

Consider the sequence ${a_n}$ where: $a_1 = 1$; the sequence is increasing, meaning $a_k > a_{k-1}$ for any $k > 1$; the first-order differences are increasing, meaning $a_k – a_{k-1} > a_{k-1} – a_{k-2}$ for any $k > 2$; The terms in the sequence and the first-order differences uniquely cover the set of non-zero natural numbers (i.e., any non-zero natural number appears either in the sequence ${a_n}$ or in the first-order differences sequence, but not in both). Thus $a = \{1, 3, 7, 12, 18, 26, 35, 45, \dots\}$, and the first-order differences are $\{2, 4, 5, 6, 8, 9, 10, \dots\}$. These two sequences are disjoint and cover the set of non-zero natural numbers. Given a natural number $n$, determine $a_n$.

## Input data

The input file hof.in contains a single line which contains the natural number $n$.

## Output data

The output file hof.out contains a single line which contains the natural number $a_n$, representing the $n$-th term in the Hofstadter sequence.

## Constraints

$1 \leq n \leq 100\ 000\ 000$

## Example

`hof.in` `hof.out`  
`5` `18`