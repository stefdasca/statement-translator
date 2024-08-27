## Task
Given the initial state of the game, determine who wins, assuming both players play optimally.

## Input data

The input file `tanakagame.in` contains on the first line the number of games $T$, followed by the descriptions of the $T$ games. The first line corresponding to a test case contains 3 numbers $N, M, K$ with the meanings from the problem statement. The next $N$ lines of the test case contain $M$ numbers each, representing the values of the elements in the matrix.

## Output data

The output file `tanakagame.out` contains the corresponding responses for the games, each response on its own line. For each game, the message Tanaka is printed if Tanaka wins, or Uivlis if Uivlis wins.

## Constraints and clarifications

1 $ \leq N, M \leq $ 50

1 $ \leq K \leq $ 100

0 $ \leq$ values in the matrix $ \leq $ 99

1 $ \leq T \leq $ 40

For 10 points, $N = M = K = 1$

For another 10 points, $N = 1, M = 2, K = 2$

For another 20 points, $N = 1, K = M$

For another 40 points, $K = 100$

## Example

`tankagame.in`
```
5
1 1 1
4
1 2 2
72 40
1 1 5
99
3 4 100
56 75 56 29
55 95 87 83
71 98 27 24
3 4 4
95 13 22 1
69 55 99 80
65 70 75 10
```

`tankagame.out`
```
Uivlis
Uivlis
Tanaka
Uivlis
Tanaka
```

## Explanation

In the first game, after Tanaka's move, the only position in the matrix will contain either $1$, $2$, or $3$. In any case, Uivlis can move such that the result is $0$, in which case Tanaka loses.