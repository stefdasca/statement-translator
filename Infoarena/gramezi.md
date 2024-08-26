## Task

Zaharel and Bronzarel are playing the following game: there are $N$ piles of coins on the table. It is known that if Zaharel takes pile $i$, he receives $A_i$ coins from that pile, and if Bronzarel takes pile $i$, he receives $B_i$ coins from that pile (it is known that each pile has at least $\max(A_i, B_i)$ coins and the remaining coins are discarded). The two players take turns picking a pile, until all $N$ piles are exhausted, and Zaharel is the first to take a pile. At the end, the player with more coins wins. If the coin quantities are equal, the game is considered a draw. Knowing that Zaharel and Bronzarel play optimally, determine the number of coins each player will have at the end. By optimal play, it is understood that each player tries to maximize the difference between the number of coins they own and the number of coins the other player owns, and if there are multiple ways to achieve the same difference, they will try to maximize their number of coins.

## Input data

The input file `gramezi.in` contains the natural number $N$ on the first line. The next $N$ lines each contain two natural numbers separated by a space, representing the values $A_i$ and $B_i$ respectively.

## Output data

The first line of the output file `gramezi.out` will contain two natural numbers separated by spaces representing Zaharel's score and Bronzarel's score, respectively.

## Constraints

$1 \leq N \leq 30\ 000$  
$1 \leq A_i, B_i \leq 30\ 000$

## Example

`gramezi.in`  
4  
2 10  
5 5  
7 3  
4 1

`gramezi.out`  
9 6

## Explanation

Zaharel takes pile 1, then Bronzarel takes pile 2, then Zaharel takes pile 3, then Bronzarel takes pile 4. Another possible game with the same score difference is the following: Zaharel takes pile 1, then Bronzarel takes pile 3, then Zaharel takes pile 2, then Bronzarel takes pile 4. Thus, the scores 7 and 4 respectively would have been obtained, but these are smaller than in the first variant.