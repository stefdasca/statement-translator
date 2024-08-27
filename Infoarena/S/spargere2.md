## Spargere2

Georgică is a greedy guy. Robbing the Georgelonia bank is nothing compared to his new grand plan. This time, Georgică plans to rob Petrilonia, the great rival of the Georgelonia bank. Similar to the Georgelonia bank, Petrilonia has $N$ safes, numbered from $1$ to $N$. In each safe $i$ there is a sum of money $v[i]$. Because it's Round 4 and because it's Petrilonia, this sum of money is not necessarily positive. We define the distance between two safes $i$ and $j$ as $|i - j|$. Georgică knows that if he opens two safes that are at a distance strictly less than $K$, the alarm will go off. When Georgică opens a safe, he is obliged to take all the money from that safe.

## Task

Georgică wonders what is the maximum amount of money he can steal from the Petrilonia bank during Round 4 without setting off the alarm.

## Input data

The input file `spargere2.in` contains on the first line two natural numbers $N$ and $K$, having the meaning as described. The second line contains $N$ natural numbers $v[i]$.

## Output data

The output file `spargere2.out` will contain a single natural number, representing the answer to Georgică's question.

## Constraints and clarifications

$1 \leq K \leq N \leq 100,000$

$-10^9 \leq v[i] \leq 10^9$

Georgică can leave the bank without opening any safe if this is a wise decision. In this case, his profit will be equal to $0$.

## Example

`spargere2.in`

```
4 2
1 -1 10 4
```

`spargere2.out`

```
11
```

## Explanation

Georgică is not allowed to empty two safes that are at a distance strictly less than $2$. In other words, Georgică is not allowed to empty two consecutive safes. The maximum profit is obtained by emptying safe $1$ and safe $3$.