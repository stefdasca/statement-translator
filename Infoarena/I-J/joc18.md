## Game 18

Because they got bored, Aurel and Bianca decided to play the following game: Initially, they have $N$ natural numbers, $x_1$, $x_2$, $\dots$, $x_N$. At each turn, the player who is to move chooses any number of the $N$ numbers, provided that they choose at least one number and do not choose all of them, and divides each chosen number by a divisor of it greater than $1$. Players alternate turns, and the player who cannot make a valid move loses. Bianca makes the first move. Determine the winner of the game considering that both players play optimally.

## Input data

The input file `joc18.in` will contain on the first line $T$, the number of tests. Each test will contain on its first line the natural number $N$ as described in the statement. The next line contains the $N$ natural numbers separated by a space.

## Output data

In the output file `joc18.out`, $T$ lines will be printed, with the name of the player who wins the game described in test $i$ ("Aurel" or "Bianca").

## Constraints

$1 \leq T \leq 10$

$2 \leq N \leq 10^5$

$1 \leq x_i \leq 10^6$ for $i = 1 \dots N$

## Example

`joc18.in`

``` 
1 
2 
1 2 
``` 

`joc18.out`

``` 
Bianca 
``` 

## Explanation

Bianca divides the number $2$ by $2$, and Aurel cannot make any valid moves afterwards.