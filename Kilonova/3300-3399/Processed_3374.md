
# Task

Strikakef went to his brother who was playing chess and made a bet with him. Strikakef placed a coin on the chessboard in every cell with heads up, except for the one in the bottom left corner where he placed it tails up. Strikakef bet that his brother could not empty the board by performing the following process:
<br>
As long as there are still coins on the board, choose a coin with tails up, remove it, and flip all adjacent coins (on the same row or column) to the one removed. If there are still coins and none is tails up, his brother loses.
<br>
You are given $T$ pairs of numbers $N, M$ and you must answer for each pair whether his brother has a strategy to empty the chessboard which is $N$ by $M$ squares.

# Input data

The first line contains the number $T$, and on the next $T$ lines, there are $2$ numbers with the meaning from the statement.

# Output data

$T$ lines will be printed, each line containing the corresponding answer for each question. The answer is "YES" if his brother can empty the board, the answer is "NO" if he cannot empty it.

# Constraints and clarifications

* $1 \leq T \leq 10^5$;
* $1 \leq N,M \leq 10^9$;
* Messages such as "YeS", "no", "YES" ... are considered **incorrect**.
* For $20$ points: $1 \leq T, N, M \leq 4$;
* For another $30$ points: $1 \leq T, N, M \leq 100$.

# Example 1

`stdin`
```
3
1 1
2 2
1 4
```

`stdout`
```
YES
NO
YES
```

## Explanation

For the first test, he only has to remove the single coin from the board.  
For the second test, it can be shown that he cannot empty the board.  
For the third test, the board is just a row, he can take the squares one after another and in the end, the board will be empty.
```
