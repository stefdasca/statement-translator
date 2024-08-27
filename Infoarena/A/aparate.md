# Slots

While the world is in quarantine, $K_0 K$ alaru $47$ returns to his habitat (that is here, at Junior Challenge). Nature is healing. Since we last saw him, he has gone through many adventures. After winning money from previous editions of $JBOI$, the first thing he did was gamble (and lost it all). While he recounts in detail what he played, he challenges you to calculate the massive losses he incurred. At the beginning, he describes the machine he played on. It is a matrix with $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$) with integer values. $K_0 K$ alaru $47$ starts recounting $Q$ events in chronological order. The events are as follows: "Hits the middle button violently (or screen, or machine, or whatever)" - we'll call it an update - and the columns with indices $l, l + 1, l + 2, \ldots, r$ rotate upward by $k$ values. "You get angry, because 'you were unlucky' and lost much more than you should have" - we’ll call it a query - the cells at coordinates $(k, l), (k, l + 1), (k, l + 2), \ldots, (k, r)$ light up, and you lose an amount of money equal to the sum of the lit cells. The cells do not remain lit until the end of the game. After this operation, they turn off again. To prove to $K_0 K$ alaru $47$ that you paid attention to his story, you want to tell him how much money he lost at each query operation.

## Input data

In the input file `aparate.in`, the first line contains the numbers $N, M$, and $Q$ as described in the statement. The next $N$ lines contain $M$ numbers each, representing the initial matrix. The next $Q$ lines will contain $4$ numbers $tip \space l \space r \space k$ separated by a space, representing an event:
- If $tip$ is $1$, then the respective event is an update and the columns with indices from $l$ to $r$ rotate upwards by $k$ values.
- If $tip$ is $2$, then the respective event is a query, to which you must respond with the sum of the elements on line $k$ and columns with indices from $l$ to $r$.

## Output data

In the output file `aparate.out`, the answers to all of $K_0 K$ alaru $47$'s query operations will appear on separate lines in order.

## Constraints

$2 \leq N$  
$2 \leq M$  
$N * M \leq 100.000$  
$Q \leq 50.000$  
$1 \leq l \leq r \leq M$ for each event  
$1 \leq k \leq N$ for each event  
$1 \leq type \leq 2$ for each event  
Elements in the matrix are values from $1$ to $1.000.000$.  
Note that since the values are positive, $K_0 K$ alaru $47$ never has 'negative' losses, so he can never win money. Let $A[1][c], A[2][c], \ldots, A[N][c]$ be the elements of column $c$. An 'upward' rotation of the respective column by one position means that the element $A[1][N]$ is eliminated, all other elements move up by one position, and the position that is vacated at the very bottom will be replaced by the eliminated element. Thus, the elements of the column will be (from top to bottom) $A[2][c], A[3][c], \ldots, A[N][c], A[1][c]$. An upward rotation by $k$ positions of a column means that we rotate the respective column upward $k$ times. $K_0 K$ alaru $47$ does not recommend anyone to have his experience.

## Subtasks

Subtask $1$ ($10$ points, tests $1-2$): $Q \leq 1.000$  
Subtask $2$ ($20$ points, tests $3-6$): $M \leq 1.000$  
Subtask $3$ ($30$ points, tests $7-12$): $N = 2$  
Subtask $4$ ($40$ points, tests $13-20$):

## Initial constraints

## Example

`aparate.in` 
```
4 6 5
1 3 5 2 6 7
3 4 9 2 1 9
1 1 1 1 1 1
9 9 7 7 7 9
1 3 5 2
1 2 5 3
2 1 6 3
2 4 6 1
2 1 6 1
```

`aparate.out`
```
10
3
27
```

## Explanation

Initially, the matrix looks like this: 
```
1 3 5 2 6 7
3 4 9 2 1 9
1 1 1 1 1 1
9 9 7 7 7 9
```
After the first operation, it will look like this: 
```
1 3 1 1 1 7
3 4 7 7 7 9
1 1 5 2 6 1
9 9 9 2 1 9
```
After the second operation, it will look like this:
```
1 9 9 2 1 7
3 3 1 1 1 9
1 4 7 7 7 1
9 1 5 2 6 9
```
The answer to the third operation will be $2 + 1 + 7 = 10$.  
The answer to the fourth operation will be $1 + 1 + 1 = 3$.  
The answer to the fifth operation will be $1 + 4 + 7 + 7 + 7 + 1 = 27$.