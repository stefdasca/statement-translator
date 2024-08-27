# Tritzi

A trit is a logical unit that can take 3 values: $0$, $1$, and $2$. Trits can be used exactly like bits (which you’ve probably heard of). For example, information can be transmitted as sequences of trits. To avoid confusion with bit sequences, trit sequences have a special property: two trits with the values $0$ and $1$ respectively cannot be transmitted one after another. Thus, there are valid and invalid trit sequences (which contain at least one pair of adjacent trits equal to $0$ and $1$). For example, the sequence $02212212000211$ is a valid sequence, but the sequences $0122212$ or $2221022$ are not valid. Determine the number of valid trit sequences of length $N$. Since this number can be very large, we are only interested in its value modulo a number $P$.

## Task

## Input data

The first line of the input file `tritzi.in` contains the integer $T$, representing the number of upcoming tests. The next $T$ lines contain $2$ integers each: $N$ and $P$. 

## Output data

For each test in the input file, you will print in the output file `tritzi.out` a number representing the requested value.

## Constraints and clarifications

$1 \leq T \leq 30$

$1 \leq N \leq 1\ 000\ 000\ 000$

$1 \leq P \leq 32\ 000$

## Example

`tritzi.in` and `tritzi.out`

```
4
1 997
4 997
21 997
999999999 13
3 41
22 5
```