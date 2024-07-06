Two players are playing on a $5 \times 5$ chessboard. Each square contains a non-zero number of chocolate candies. A square is considered blocked if, in all four directions, it is adjacent to squares that contain candies. The first player starts. The two players take turns. On each turn, a player selects an unblocked square and takes all the candies from that square. As a result of a move, it is possible that certain squares that were blocked become unblocked. Each player's goal is to collect as many candies as possible. Both players play optimally.

# Implementation

Your program will implement the function
```cpp
int solve_test (int *x)
```
The parameter $x$ will contain elements of an array indexed from $0$, containing the $25$ numbers from the chessboard. The function must return the maximum number of candies that the first player will collect from the board.

The grader will alternately call your function and a similar function implemented by the committee on various tests, multiple times in the same run, and will measure the sum of the times taken by both functions. The score you will receive depends on the ratio between the two total times (your time and the committee's time).

In addition to the function you will implement, you can declare local or global variables and implement other helper functions. It is recommended that global variables and functions be declared with the static modifier.

# Constraints and clarifications
* The numbers on the board are positive, non-zero, distinct, and do not exceed $35\ 000$.
* If, as a result of a call, the returned answer from your function is incorrect, you will get $0$ points.
* **Your function will be called multiple times within the same run. Pay attention to possible reinitializations of variables!!!**

# Example

Board sent as parameter:
```
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```
Returned value:
```
169
```
## Explanation
The first player will take the odd numbers from the board in descending order. The second player will take the even numbers in descending order.

# Scoring method
**The scoring method differs from the one during the contest!**
The contestant's score will be calculated as follows:
Let $r$ be the time ratio per test between the contestant's source and the committee's source
* If $r > 50$, the score awarded will be $0$
* If $40 < r \leq 50$, the score awarded will be $30$
* If $15 < r \leq 40$, the score awarded will be $((40 - r) \times 70 + (r - 15) \times 30) / 25$
* If $10 < r \leq 15$, the score awarded will be $70$
* If $5 < r \leq 10$, the score awarded will be $((10 - r) \times 100 + (r - 5) \times 70) / 5$
* If $0 < r \leq 5$, the score awarded will be $100$