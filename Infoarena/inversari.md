## Task

Besides his old artistic passions, Zuru now has a passion for inversions. His philosophy professor provides him with a sequence $A$ containing $N$ natural numbers. Then, he asks $M$ questions of the form: how many inversions are contained in the subarray of the array $A$ found between positions $i$ and $j$ $(i \leq j)$. Because he is a perfectionist, Zuru asks for your help to answer each of the questions posed by the professor. Zuru has also thought it would be good to tell you how he defines an inversion. In his view, an inversion is a pair of indices $(p, q)$ with $p < q$ such that $A_p > A_q$.

## Input data

The input file `inversari.in` contains on the first line $N$ and $M$, separated by a single space, having the meaning described above. The next line contains the $N$ natural numbers of the sequence $A$, separated by a single space. The following $M$ lines contain the questions posed by the professor, each line containing two numbers separated by a space, $i$ and $j$ $(i \leq j)$, the endpoints of the subarray.

## Output data

The output file `inversari.out` contains $M$ lines, each line containing the answer to the professor's questions, in the order in which they appear in the input file.

## Constraints and clarifications

$1 \leq N \leq 5000$

$1 \leq M \leq 100\ 000$

Elements of the array $A$ are natural numbers less than or equal to $100\ 000$

For $50\%$ of the tests $N \leq 1000$

For $50\%$ of the tests elements of the array $A$ are natural numbers less than or equal to $30$

## Example

`inversari.in`
```
5 5
4 2 5 3 1
1 5
2 4
3 5
1 3
2 3
```

`inversari.out`
```
7
1
3
1
0
```