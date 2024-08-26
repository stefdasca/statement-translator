## Task

This problem has been taken from atcoder: F - Prime Flip Mr. J. arrived in Vegas this week. If you haven't met Mr. J. yet, don't worry; all you need to do to get into his inner circle is to exist and help him with a little problem, but all in good time. Mr. J.'s favorite game is one reserved for connoisseurs, so we won't burden you with its name. As for the rules, they couldn't be simpler. On a table, there are an infinite number of cards, numbered from $1$. Initially, the cards $x_1$, $x_2$, $\dots$ $x_N$ are face up, and all the others are face down. The player can apply the following operation to the cards as many times as they want: Choose a prime number $p \geq 3$. Then choose $p$ consecutive cards and turn each of them over. The player wins if they manage to turn all the cards face down in a minimum number of moves. This is where you come in. Help Mr. J. find out the minimum number of moves needed to win on a given table!

## Input data

The input file `vegas.in` contains $T$ tests. The first line of the file contains $T$, the number of tests in the file. Each test consists of two lines. The first of these contains $N$, the number of cards that are face up. The second line of the test contains, in ascending order, separated by space, the $N$ cards.

## Output data

The output file `vegas.out` will contain $T$ lines. On the $i$-th line, print the minimum number of operations Mr. J. needs to win on the table described in the $i$-th test from the input file.

## Constraints

$1 \leq T \leq 6$

$1 \leq N \leq 100$

$1 \leq x_1 < x_2 < \dots < x_N \leq 10^7$

### Subtasks

Subtask | Points | Constraints 
------- | ------- | -----------
1       | 1 point | $1 \leq N \leq 10$ 
2       | 1 point | $1 \leq N \leq 20$ 
3       | 1 point | $1 \leq x_N \leq 200$ 
4       | 2 points | No additional constraints 

## Example

`vegas.in`

```
2
2
1 2
6
3 4 5 6 7 9
```

`vegas.out`

```
2
4
```

## Explanation

In the first test of the example, the first operation is to flip the sequence of cards $1-5 \Rightarrow$ the cards face up will be: $3$, $4$, $5$. The second operation is to flip the cards in the sequence $3-5 \Rightarrow$ all the cards turn face down. In the second test of the example: After the sequence: $8-12 \Rightarrow$ the cards face up: $3$ $4$ $5$ $6$ $7$ $8$ $10$ $11$ $12$ After the sequence: $10-12 \Rightarrow$ the cards face up: $3$ $4$ $5$ $6$ $7$ $8$ After the sequence: $3-13 \Rightarrow$ the cards face up: $9$ $10$ $11$ $12$ $13$ After the sequence: $9-13 \Rightarrow$ all the cards are face down