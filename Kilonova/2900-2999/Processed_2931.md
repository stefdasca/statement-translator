All of us have heard of Yeti, the creature that lives in the Himalaya Mountains. However, not many know about his enemy, Yatti.

Yatti lives in the Maldives Archipelago, by the sea. He has lived in peace for thousands of years on an island, but due to global warming and the rising sea levels, he has to move to another island.

There are $26$ islands he can move to, marked with the $26$ uppercase letters of the Latin alphabet (`A`, `B`, `C`, ..., `X`, `Y`, `Z`).

Yatti has $N$ friends, each residing on one of the $26$ islands. He knows that the $i$-th friend lives on the island $a_i$. He wants to move to an island where the most of his friends live. If there are multiple islands with the same number of people, he will move to the smallest one in alphabetical order.

# Task

Given $N$ and the sequence $a_1, a_2, \dots, a_N$. Additionally, Yatti will ask $Q$ queries in the form: *If I only had friends living on the positions $a_l, a_{l+1}, a_{l+2}, \dots, a_r$, on which island would I move?* (Read the example explanations for clarification).

# Input data

The first line of the input file ```yatti.in``` contains the number $N$. The second line contains the sequence $a_1, a_2, \dots, a_N$. The third line contains the number $Q$, and the following $Q$ lines each contain a pair $l, r$ separated by a space. 

# Output data

Print in the output file ```yatti.out``` $Q$ lines, each line containing the answer to the $i$-th query.

# Constraints and clarifications
* $2 \leq N, Q \leq 100\ 000$
* $a_i \in \{$`A`$, `B`$, `C`$, \dots, `X`$, `Y`$, `Z`$\}$ for each $i$ from $1$ to $N$

|#|Score|Constraints|
|-|-|--------|
|1|20|$Q = 1$, $l = 1$, $r = N$|
|2|20|$N, Q \leq 1\ 000$|
|3|30|$a_i \in \{$`A`$, `B`$\}$|
|4|30|No additional constraints|

# Example 1
`yatti.in`
```
9
ABBAGAGGE
6
1 9
1 4
2 3
5 8
4 7
9 9
```
`yatti.out`
```
A
A
B
G
A
E
```

## Explanations

In the first query, we need to determine which island Yatti would move to if we consider all the values in the sequence $A$. We see that both `A` and `G` appear $3$ times. Since `A` comes before `G` in alphabetical order, Yatti would move to island `A`. 

In the fourth query, we consider the values $a_5, a_6, a_7, a_8$, which are `G`, `A`, `G`, `G`. If he moved to island `A`, he would be with one friend, but if he moved to island `G`, Yatti would be with $3$ friends. Thus, he prefers to move to island `G`.

In the last query, we only consider the value $a_9 = $ `E`. Therefore, he would move to island `E`.

# Example 2
`yatti.in`
```
5
ABBAB
3
1 5
2 4
1 4
```
`yatti.out`
```
B
B
A
```