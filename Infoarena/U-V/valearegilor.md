## Task

I built brick upon brick Until I reached the top of the pyramid Many of us remain awestruck by the grandeur of the only one of the Seven Wonders of the Ancient World that has lasted through the ages. However, few of us actually know how the pyramids were built. Recent historical data shows that during the Pharaoh's time, people lived in extreme poverty, with the unemployment rate being $100\%$. The question remains: How did the Pharaoh get money to build the pyramids? From loan sharks, of course (those who smuggled stolen problems). Said and done, the Pharaoh borrowed money from them and built the tallest and most beautiful pyramids in the world at that time, and the remaining money he lost in gambling, Book of Ra of course. The problem followed when he had to repay the money $\ldots$ Luckily, the Pharaoh had $n$ fingers. The lengths of his fingers were pairwise distinct and formed a permutation. As the deadline approached, the loan sharks called the Pharaoh and told him that if he did not repay the money they would choose an interval $\left[ l_i, r_i \right]$ of his fingers and, with each delay, would choose from this interval a finger $p_{i+1}$ with the property that $p_i < p_{i+1} > p_{i+2}$ which they would cut off until such a finger no longer existed. Frightened, the Pharaoh wants to know the answer to $q$ questions: If the loan sharks were to choose the interval $\left[ l_i, r_i \right]$, how many fingers would remain in this interval in the end?

## Input data

The input file `valearegilor.in` contains on the first line the numbers $n$ and $q$. On the next line, the lengths of the fingers are found in the form of a permutation $p_1, p_2, \dots, p_n$. The following $q$ lines describe the questions in the form $\left[ l_i, r_i \right]$.

## Output data

In the output file `valearegilor.out` you will print the answer to the Pharaoh's $q$ questions, one per line.

## Constraints and clarifications

$1 \leq n \leq 100\ 000$

$1 \leq q \leq 1\ 000\ 000$

$1 \leq l_i \leq r_i \leq n$

It will be considered that the fingers $l_i - 1$ and $r_i + 1$ have infinite length within a question.

## Example

`valearegilor.in`
```
15 4
1 2 3 4 5 10 8 6 7 9 14 13 11 12 15
1 5
3 3
10 14
4 15
```

`valearegilor.out`
```
5
1
3
8
```