```markdown
We define a double permutation of order `n` as a sequence consisting of the first `2n` positive natural numbers: $(a_1, a_2, ... , a_n, a_{n+1}, a_{n+2}, ... , a_{2n})$. This double permutation is thrice increasing if the following three properties hold true:
1. The sequence formed from the first `n` elements is increasing: $a_1 < a_2 < ... < a_n$
2. The sequence formed from the last `n` elements is increasing: $a_{n+1} < a_{n+2} < ... < a_{2n}$
3. The ordered pairs formed from elements at identical positions in the two sequences are also in increasing order: $a_1 < a_{n+1}, a_2 < a_{n+2}, ... , a_n < a_{2n}$.

For example, the permutation `(1,3,4,2,5,6)` is a double permutation of order `3`, thrice increasing because the sequences `(1,3,4)` and `(2,5,6)` form increasing sequences, and all pairs formed from elements at identical positions: `(1,2), (3,5), (4,6)` also form increasing sequences.

The following double permutations do not have the thrice increasing property:
`(1,4,3,2,5,6)` – the sequence `(1,4,3)` is not increasing,
`(1,3,4,2,6,5)` - the sequence `(2,6,5)` is not increasing,
`(1,4,5,2,3,6)` – the pair `(4,3)` is not increasing.

For simplicity, a double permutation thrice increasing will be called a permutation henceforth.

We will consider all permutations of order $n$ ordered lexicographically, numbered starting from `1`. The table below contains the data for $n=3$:
position permutation
| position | permutation   |
|----------|---------------|
| 1        | 1 2 3 4 5 6   |
| 2        | 1 2 4 3 5 6   |
| 3        | 1 2 5 3 4 6   |
| 4        | 1 3 4 2 5 6   |
| 5        | 1 3 5 2 4 6   |

There are two types of questions:
1. What permutation is at a given position?
2. At what position is a given permutation?

The first question is coded as follows: `1 n p` and consists of the values 
`1` – the type of question, 
`n` – the order of the permutation, 
`p` – the requested permutation's position.

The second question is coded as follows: $2\\ n\\ a_1\\ a_2\\ \\dots\\ a_{2n}$ and consists of the values 
`2` – the type of question, 
`n` – the order of the permutation, 
$a_1\\ a_2\\ \\dots\\ a_{2n}$ – the elements of the permutation.

# Examples
The question `1 3 2` means:
“What permutation of order `3` is at position `2` in lexicographic order?” and has the answer: `1 2 4 3 5 6`.
The question `2 3 1 3 5 2 4 6` means:
“At what position is the permutation of order `3`: `1 3 5 2 4 6`?” and has the answer: `5`.

# Task
Respond correctly to a set of questions.

# Input data
The file `permutare.in` contains on each line a question of any type.

# Output data
The file `permutare.out` will contain on each line an answer to each question from the input file, in the order of the questions.

# Constraints and clarifications
* `2 < n < 1\ 000`;
* `0 < p \\leq 1\ 000\ 000\ 000` (in the case of type `1` questions);
* the answer to type `2` questions is `\\leq 1\ 000\ 000\ 000`;
* input files will contain at most `2\ 000` questions;
* for tests worth `20` points, the number of questions will be `1\ 000` and the order numbers involved in the calculations will be less than `5\ 000`;
* for tests worth `30` points, the questions will be of type `1`;
* for tests worth `30` points, the questions will be of type `2`;
* for tests worth `30` points, the questions will be mixed.
* The problem will be evaluated on tests worth `90` points.
* `10` points will be awarded automatically.

# Example

`permutare.in`
```
1 3 2
2 3 1 3 5 2 4 6
1 4 1
2 4 1 2 3 4 5 6 7 8
```

`permutare.out`
```
1 2 4 3 5 6
5
1 2 3 4 5 6 7 8
1
```
Explanations
---

- The second permutation of order `3` `(1,2,4,3,5,6)`
- The permutation `(1,3,5,2,4,6)` is at position `5`
- The first permutation of order `4` `(1,2,3,4,5,6,7,8)`
- The permutation `(1,2,3,4,5,6,7,8)` is at position `1`
```