# Crabs

Antoniei loves crustaceans very much. Since it is impossible for Antonio to gift her a real crab, he thought of naming this problem... Crabs. Given a number $N$ and $N$ words consisting only of lowercase English letters.

## Task

Calculate the longest subsequence of words in the initial sequence that satisfies the following properties:
- For any $i , 1 \leq i \leq M-1$, the last character of $C_i$ is equal to the first character of $C_{i+1}$.
- For any $i , 1 \leq i \leq M-1$, $P_{i+1} - P_i \leq K$, for a given $K$.

Where $M$ is the length of the new resulting sequence, $C_i$ is the word at position $i$ in the new sequence, and $P_i$ is the position of word $C_i$ in the initial sequence.

## Input data

The input file `raci.in` will contain on the first line two values, $N$ and $K$, as described above. The second line of the file will contain the $N$ words separated by exactly one space.

## Output data

The output file `raci.out` will contain a single value representing the length of the longest subsequence of words that respects the two properties specified in the statement.

## Constraints and clarifications

$1 \leq N \leq 500\,000$  
$1 \leq K \leq N$  
$2 \leq length$ of any word $\leq 10$  

## Example

`raci.in`
```
11 3
aa ab bc dd db be ff fg eh gi hj
```
`raci.out`
```
5
```

## Explanation

The longest subsequence is: $aa$ $ab$ $bc$ $dd$ $db$ $be$ $ff$ $fg$ $eh$ $gi$ $hj$.