# Balance

Chernel the Pawnbroker has a problem. He received $N$ identical coins from a client, supposedly made of gold, but he suspects that exactly one of them is fake. Chernel knows that the fake coin is either heavier or lighter than the gold ones, which all have equal mass. To check, he uses a balance scale and performs $M$ weighings. In each weighing, he places an equal number of coins on the two pans and records the result. Unfortunately, Chernel acts quite chaotically, and in the end, he does not know if the weighings can precisely determine the fake coin. Help him find the answer! 

## Input data

The first line of the input file contains two integers $N$ and $M$.  
The next $M$ lines each describe a weighing:
- a number $k$, representing the number of coins placed on each of the two pans of the balance
- $k$ integers between $1$ and $N$ representing the coins placed on the left pan
- another $k$ integers between $1$ and $N$ representing the coins placed on the right pan
- along with a number $r$ from the set $\{0, 1, 2\}$.

$r$ indicates the result of the weighing: $0$ if the balance remains equal, $1$ if the left pan is heavier than the right, and $2$ if the right pan is heavier than the left.

## Output data

The first line of the output file contains an integer between $1$ and $N$, representing the fake coin if it can be determined precisely, or $0$ if Chernel's weighings were not sufficient to find the coin.

## Constraints and clarifications

$$1 \leq N, M \leq 1024$$

## Example

`balanta.in`  
`8 3`  
`4 1 2 3 4 5 6 7 8 1`  
`1 1 2 0`  
`1 3 4 2`

`balanta.out`  
`2`