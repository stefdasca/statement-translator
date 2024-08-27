## Task

Because the first punishment was not enough, Antonia will ask Antonio $Q$ more questions: Dear Antonio, I will give you a natural number $N$. You must know that this number was initially equal to $1$. I want you to tell me in how many ways we could obtain the number $N$ through exactly $K$ multiplication operations, all of these with even numbers. So that you also have time to buy me tulips, I ask for this number modulo $666013$. Two ways of obtaining a number are considered distinct if there is at least one operation out of the $K$ that is different. For example: 1 $\times$ 6 $\times$ 2 differs from 1 $\times$ 2 $\times$ 6 because the first operation in the first mode of obtaining is a multiplication by 6, while the first operation in the second mode of obtaining is a multiplication by 2.

## Input data

The input file `totoluna.in` contains on the first line a natural number $Q$, representing the number of questions from Antonia. Each of the following $Q$ lines contains two natural numbers $N$ and $K$, separated by a space, with the meaning from the task description.

## Output data

The output file `totoluna.out` will contain $Q$ lines. Each line $i$ will contain a single natural number, representing the answer to Antonia's $i^{th}$ question.

## Constraints and clarifications

$1 \leq Q \leq 100$

$1 \leq N \leq 10^{12}$

$1 \leq K < 50$

## Example

`totoluna.in`

```
2
5 1
10 1
```

`totoluna.out`

```
0
1
```

## Explanation

The number 5 cannot be obtained according to the task. The number 10 can be obtained only by a multiplication by 10.

`1 60 2 4`

The 4 possibilities are: $1 \times 2 \times 30$, $1 \times 30 \times 2$, $1 \times 6 \times 10$, $1 \times 10 \times 6$.