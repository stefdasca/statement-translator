Gică and Petrică live in the Merry Town. There exists a street network that contains only one-way streets, and to travel between any two intersections, you must pay a specific fee for each intersection and each street you pass through (including the intersection you leave from and the intersection you arrive at). These fees do not bother anyone, as they are natural monetary values between `0` and `10`. The two are not interested in the actual map of the Town but have found the table of minimum sums they must pay to travel between any two intersections, and they have thought to use it to play an interesting game (This matrix contains only finite values).

Thus, having the matrix `A` where `A[i, j]` represents the minimum cost to reach intersection `j` from intersection `i` (`A[i, i]` is the fee to be paid at node `i`), each of the two players alternately moves as follows: the player at turn chooses a strictly positive natural number `k` and subtracts `k` from all elements of a row or column of the matrix, provided that all elements of the matrix remain non-negative. Gică moves first, and the player who, when it is their turn, can no longer make a valid move, loses. It is considered that the two friends play perfectly, meaning that if one of them ever has a winning strategy regardless of the opponent's moves, they will not make a move that would lead to the loss of any winning strategy.

# Task
Given the matrix `A` with the significance described, determine which of the two is the winner of the game.

# Input data
The file `joc.in` contains between `1` and `20` sets of input data. The first line of each set contains a positive natural number `N` representing the dimensions of matrix `A`, and on the following `N` lines, there are `N` natural numbers, representing the elements of matrix `A`. `N = 0` marks the end of the sets of data that make up the input file.

# Output data
The output file `joc.out` will contain a number of lines equal to the number of data sets. On each of these lines is one of the values: `1` if the respective game is won by Gică, `2` if the respective game is won by Petrică.

# Constraints and clarifications
* `1 \leq number of tests \leq 20`
* `2 \leq N \leq 100`
* Correctly solving the tests containing at most `10` data sets with `N \leq 5` guarantees obtaining `50%` of the score.

# Example

`joc.in`
```
2
8 25
25 9
2
3 8
9 3
0
```

`joc.out`
```
1
2
