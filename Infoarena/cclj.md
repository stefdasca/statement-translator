# With the Horse at JBOI

The fearless $K0K \,alaru \,47$ has struck again. He has qualified for the renowned international competition $JBOI$. Since $K0K \,alaru \,47$ invested heavily in his preparation to become a true Olympian, he no longer has the means to attend the competition, so he borrowed a horse from his neighbor, Sorinel. $K0K \,alaru \,47$ is not good at geography, so it is your duty to help him reach the event. But guess what! He has become so good in the last year that if he arrives at the competition, he will achieve MAXIMUM (and obviously the first place). This must not be allowed to happen (only the Romanian team is allowed to take MAXIMUM), so you need to give $K0K \,alaru \,47$ the longest route possible to ensure he doesn't arrive at $JBOI$ on time. Unfortunately, although he is terrible at geography, he has an excellent memory. Therefore, you need to give him a long route that does not pass through the same place more than once (otherwise, he will realize you have tricked him). The area in which $K0K \,alaru \,47$ can travel (since he has some issues with identification papers and is not allowed to leave the Eastern European region) is in the shape of an $N \times M$ board. The horse of $K0K \,alaru \,47$ can only move in an $L$ shape (just like all the horses in the world). Your goal is to generate a sequence of knight moves of maximum cardinality. You can start and end anywhere, but your score will account for whether you start and/or finish in corners.

## Task

## Input data

The input file $cclj.in$ contains a number $t$ indicating the number of tests. The following $t$ lines each contain two numbers $N$ and $M$ separated by a space, representing the dimensions of the board.

## Output data

The output file $cclj.out$ contains the answer for each test. The first line of each test contains the number $K$ signifying the number of squares that $K0K \,alaru \,47$ will pass through. The next $N$ lines each contain $M$ numbers representing a matrix $A$ encoding the $K$ squares in the following way: the path of $K0K \,alaru \,47$ starts where $A[i][j]$ is $1$, continues where it is $2$, $\dots$, and finishes where the value is $K$. If a square is not visited, you must print $0$. In the matrix $A$ there must be no number other than $0$ that appears more than once. Also, all numbers must be integers in the interval $[0, K]$.

## Constraints

$1 \leq t \leq 10$

$8 \leq N, M \leq 500$

Full Feedback!

Subtask 1 (20 points): $N, M \leq 20$

Subtask 2 (20 points): $N = M$, $N$ leaves a remainder of $1$ when divided by $4$

Subtask 3 (20 points): $N = M$, $N$ is a power of $2$

Subtask 4 (40 points):

## Initial constraints

## Scoring

The score obtained on a test is: $Score = \frac{K}{MaxNr} \times Pointspertest$, where $K$ is as described above, $MaxNr$ is the maximum number of squares that can be passed under the above conditions, and $Pointspertest$ represents how many points the test is worth $(70\%\ \text{of the maximum score awarded to the test if neither end is in a corner, 85% for one end, and 100% for both ends})$. The final score is the sum of the scores obtained for each test.

## Example

`cclj.in`
```
2
10 10
8 9
```

`cclj.out`
```
7
1 0 0 0 0 0 0 0 0 0
0 2 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 6 0 0 0 0
0 0 0 0 0 0 7 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

16
1 0 9 0 7 0 0 0 0
0 0 2 0 0 0 0 0 0
3 10 0 8 0 0 0 0 0
0 6 0 0 0 0 0 0 0
5 0 0 0 0 11 4 0 0
0 0 0 0 0 0 0 0 12
0 0 0 0 15 0 0 0 0
0 0 13 0 0 0 0 0 0
0 0 0 0 0 14 0 16
```

## Explanation

Attention!

: The example does not obtain 10 points and the paths do not have optimal length.

In the example, assuming it is worth 10 points, each of the tests will be allotted 5 points. In this case, the first test will start with a score of $0.85 \times 5 = 4.25$ points, while the second test will start with a score of $1.0 \times 5 = 5$ points.