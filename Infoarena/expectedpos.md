ExpectedPos

Gigel received $K$ lists of integers for his birthday, with a total length of $N$. You might think that this is a trivial gift, but these lists are quite special: each of them is sorted in ascending order. Unfortunately, you forgot to get Gigel a gift, but he promises to forgive you if you help him answer $M$ questions in the form: "If I were to add the value $X$ to each of the $K$ lists, what would be the average position where it would be inserted to maintain the ascending order of the elements in each list?". The average position is defined as the arithmetic mean of the positions where the value $X$ is inserted. You should also know that, in ambiguous situations (when there are multiple possible positions for insertion in a list), the last such position will always be preferred.

## Task

The input file `expectedpos.in` contains on the first line the numbers $N$ and $K$, with the meaning described in the statement. Each of the next $K$ lines contains a list received by Gigel, specified in the form `c VAL 1 VAL 2 \dots VAL c` ($c$ is the number of elements, and the values after it are the elements of the list). The line $K + 2$ contains the number $M$ of questions, and the next $M$ lines contain an integer value corresponding to each question.

## Input data

The output file `expectedpos.out` will contain $M$ answers, each on a separate line. An answer will be an irreducible fraction written in the form $A/B$. Attention! There is no space between $A$, the '/' sign, and $B$. See the example for clarification.

## Output data

To solve the problem, you must adhere to the following constraints and clarifications:

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq 1000$

$1 \leq M \leq 100000$

Each list contains at least one element. Both the elements of the lists and the values $X$ that Gigel tries to insert are 32-bit signed integers. Position numbering starts from $1$.

For $70\%$ of the tests $N \leq 10000$.

## Example

`expectedpos.in`

```
10 3
1 7
6 -4 -2 0 3 3 9
3 1 3 3 2 3
```

`expectedpos.out`

```
-100
11/3
1/1
```

## Explanation

The insertion positions for the value $3$ are $1$, $6$ and $4$. Thus, the average position is $(1 + 6 + 4) / 3 = 11 / 3$. The insertion positions for the value $-100$ are $1$, $1$ and $1$, so the average position will be $3 / 3 = 1 / 1$.