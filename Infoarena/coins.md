# Coins

Captain Paftenie is an old sea wolf. He has gone through numerous adventures and has traveled the entire world. Now in his old age, he spends most of his time playing a strategy game with his first mate. The game consists of a horizontal board with $22$ squares, where coins are placed (at most one coin in each square, representing warships). Each player moves in turn. A move consists of selecting a coin and moving it to the first free square to its left. If at some step Paftenie can no longer move any pieces (all coins are aligned in consecutive positions starting from the first square), then he wins all the coins on the board. Paftenie always moves first. He has financial problems and for this reason, he would like to know the maximum number of coins he can win after a number of games.

## Task

Help Paftenie find out the result!

## Input data

The file `coins.in` contains on the first line the number $N$ of games. On the next $N$ lines, there are $22$ numbers ($0$ or $1$ - $0$ represents a free square, $1$ a square with a coin on it). The numbers are separated by a space.

## Output data

The file `coins.out` will contain on the first line an integer $M$: the maximum value found.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

The first mate always plays optimally

## Example

`coins.in`
```
4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

`coins.out`
```
5
```

## Explanation

Paftenie wins the first and the third game. Thus, he collects $5$ coins.