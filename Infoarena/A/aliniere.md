## Task

Doru, the sports teacher, now has a class with the $9$-th grade students. Being freshmen, they have quite high attendance, specifically $N$. Mr. Professor asks the students to align in ascending order of their height, but he notices that they have aligned in a line based on their friendship groups. The students do not want to leave their group or change the order within the group. Because everyone talks to everyone, Doru, being an algorithmist in his spare time, notices that each group forms a sequence and does not exactly understand what they are, so he numbers the students starting from $0$ from left to right and asks $Q$ questions of the form: "If the groups are $(0, 1, \dots, x_0 )$, $(x_0 +1, \dots, x_1 )$, $(x_1 +1, \dots, x_2 )$, $\dots$, $(x_{k-1} +1, \dots, n-1)$, what is the minimum number of groups I need to remove to be able to align the students in ascending order?" Help Doru answer the questions.

## Input data

The input file `aliniere.in` contains the natural number $N$ on the first line. The second line contains $N$ natural numbers separated by spaces, representing the heights of the students. The third line contains the natural number $Q$. Each line $i$ of the next $Q$ lines contains a natural number $K_i$ representing the number of elements in the array $x$ of the $i$-th question, followed by $K_i$ numbers representing the array $x$.

## Output data

The output file `aliniere.out` will contain $Q$ numbers, the $i$-th number representing the answer to the $i$-th question.

## Constraints

$1 \leq N \leq 100\,000$

$1 \leq Q \leq 10\,000$

$1 \leq K_i \leq 1000$, for any $1 \leq i \leq Q$

$1 \leq height_{student} \leq 10^9$ 

All $Q$ arrays “$x$” are sorted strictly in ascending order and have elements $< N-1$

Each of the $k+1$ groups forms a sequence, and students need to be sorted only by changing the order of the groups

If we remove all the groups, it is considered that we have obtained a sorted array

### For 30 points: 

$1 \leq N, K_i, Q \leq 12$, for any $1 \leq i \leq Q$

### For another 30 points: 

$1 \leq N \leq 1000$ 

$1 \leq K_i, Q \leq 100$, for any $1 \leq i \leq Q$

## Example

`aliniere.in` 

```
12
9 2 10 7 2 14 6 6 4 12 3 3 
3
3 4 9
3 1 5 10
3 2 3 30
```

`aliniere.out`

```
7
2
0
```

## Explanation

First example: For the first question, there are $7$ groups: $(9 2)$ $(10 7 2)$ $(14)$ $(6 6)$ $(4 12)$ $(3)$ $(3)$. If we remove the first, second, and fifth groups, we get the groups: $(14)$ $(6 6)$ $(3)$ $(3)$. Changing their order, we get the sorted array: `3 3 6 6 14` 

For the second question, the groups are: $(9 2 10 7)$ $(2)$ $(14 6 6 4 12)$ $(3 3)$. We can keep only the second and last group: `2 3 3` 

For the third question, the only option is to remove everything except for the last group. Thus we get the array: `3`