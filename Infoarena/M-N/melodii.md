## Task

Alinut was invited to his dear friend Alinuta's birthday party as a DJ. Five minutes before starting the mixer, he realized that he only knows $2$ songs (the first one lasts $1$ minute, and the second one lasts $2$ minutes), but he was called for exactly $N$ minutes of showtime. Since Alinut is a student at FMI and not at the Conservatory, and besides, he doesn't have much time available, this doesn't bother him too much, but he is curious to know for the $N$ minutes of performances what is the number of different ways to arrange the $2$ songs so that the performance lasts exactly $N$ minutes. For example, for $N = 4$ minutes, he has $5$ possibilities to arrange the songs: $1, 1, 1, 1$; $1, 1, 2$; $1, 2, 1$; $2, 1, 1$; $2, 2$. After calculating for $N \leq 100$ (with backtracking), he realized that this number is quite large, so he wants to know only the remainder of this number when divided by $R$, his lucky number. Additionally, he wants the answer to this question for $T$ different values of $N$.

## Input data

The first line of the input file `melodii.in` will contain the values $T$ and $R$ as described above. Each of the following $T$ lines will contain exactly one single value which will signify the number $N$ of minutes for the respective test.

## Output data

The output file `melodii.out` will contain exactly $T$ lines. On the $i$-th line will be the answer for the $i$-th question from the input file.

## Constraints and clarifications

$1 \leq T \leq 100 000$

$3 \leq R \leq 100 000$

$1 \leq N \leq 10^{18}$

For $50\%$ of the tests, $1 \leq N \leq 1\ 000\ 000$

Two subarrays of songs $a_1, a_2, \dots, a_k$ and $b_1, b_2, \dots, b_m$ are considered distinct, if $k \neq m$ or there exists an $i$ such that $a_i \neq b_i$.

$R$ is not necessarily a prime number

## Example

`melodii.in`

```
5 5
1
2
3
10
666013
```

`melodii.out`

```
1
2
3
4
2
```

## Explanation

For $N = 1$ only the song that lasts $1$ minute can be played. For $N = 2$ there are $2$ ways to arrange the songs: $1, 1$; $2$. For $N = 3$ there are $3$ ways: $1, 1, 1$; $2, 1$; $1, 2$. For $N = 10$ there are $89$ ways, and the answer is $89 \mod 5 = 4$.