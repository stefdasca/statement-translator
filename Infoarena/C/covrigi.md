## Task

The FMICUSTRESS contest takes place at the University of Bucharest. Being a particularly well-known contest, it offers a significant amount of prizes. Thus, the winner of the contest will receive a phone, the one in second place a coupon for $10$ free beers at the brewery $H$, etc. You don't really care about the prize because you're going to sell it anyway to have money to buy pretzels from Luca during the break, so you have constructed an array $V$, where $V[i]$ represents your winnings if you finish in position $i$ (how many Luca pretzels you will be able to buy). Obviously, as with any respectable contest, $V[i + 1] \leq V[i]$. To secure a better position, you have the option to buy some raspberry pi's (they are very cheap anyway), place them somewhere in the university, and "convince" those around them to let you win since the raspberry pi's will knock out their internet (the university's internal regulations explicitly state that you won't be punished until you're caught - which obviously won't happen). Specifically, you know that there are $N$ contestants participating in the contest, students are divided into $M$ rooms, a raspberry pi costs the equivalent of $K$ Luca pretzels, and with each raspberry pi you can prevent a single room from participating in the contest. You are given two arrays: $V$, representing the winnings depending on the position, and $C$, where $C[i]$ represents how many contestants from room $i$ would rank better than you if you don't stop them. How many Luca pretzels can you maximize your winnings after the contest, assuming you play optimally?

## Input data

The input file `covrigi.in` contains on the first line the numbers $N$, $M$ and $K$, with the above meanings. The next line contains the array $V$ of length $N$. The last line contains the array $C$, of length $M$. It is guaranteed that the sum of the elements in $C$ is less than $N$.

## Output data

The output file `covrigi.out` contains a single number, the maximum number of pretzels you can win.

## Constraints and clarifications

1 $ \leq N, M \leq 50000$

At least one contestant participates in the contest (you).

The numbers read are non-negative.

The numbers read from the input are less than $2^{30}$.

For tests worth $20$ points (tests $1-2$),

$M \leq 10$.

For other tests worth $30$ points (tests $3-4-5$),

$M \leq 20$.

## Example

`covrigi.in` 
```
10 4 1
10 8 5 4 4 3 2 1 1 0
2 0 0 1
```

`covrigi.out`
```
8
```

## Explanation

To maximize your profit, you can prevent room $\#1$ and $\#4$, which costs you $2 * 1 = 2$, and you finish in first place, which brings you $10$. In total, you earn $10 - 2 = 8$ pretzels.