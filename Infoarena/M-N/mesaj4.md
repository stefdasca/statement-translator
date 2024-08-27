## Task

In a game, $N$ students participate, numbered from $1$ to $N$. There are $M$ friendship relationships between students, in the form $x \; y$, meaning that the student numbered $x$ is friends with the student numbered $y$ and vice versa. Each student has a message they want to convey to all other students. To transmit the messages, at any moment in time, a single student can choose one of their friends and convey to them all the messages they have learned up to that moment. Determine the minimum time in which all $N$ students learn all $N$ messages.

## Input data

The input file `mesaj4.in` will contain on the first line two integers $N$ and $M$. The next $M$ lines contain two integers $x$ and $y$, describing a friendship relationship.

## Output data

The output file `mesaj4.out` will contain on the first line an integer $T$, representing the minimum time in which all students learn all the messages. On the next $T$ lines will be displayed two integers $x$ and $y$. The numbers on the $i$-th line represent that the student numbered $x$ conveys the known messages to the student numbered $y$ at moment $i$. If there is no solution, print $-1$.

## Constraints and clarifications

$1 \leq N, M \leq 100\,000$

For $50\%$ of the tests, $N \leq 1\,000$.

## Example

`mesaj4.in` `mesaj4.out`

```
6 8
1 2
3 1
2 5
2 3
4 5
5 1
2 6
6 4
```
```
10
1 2
3 2
5 2
4 6
6 4
5 6
4 5
2 5
1 2
3
```