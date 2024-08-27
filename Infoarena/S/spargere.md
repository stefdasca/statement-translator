# Break-in

Georgică has finished with arithmetic progressions and has found a new occupation: he decided to become a professional burglar. The first step in this career is cracking the safes of Georgelonia Bank. The bank has $N$ safes, each containing an infinite amount of money. To avoid triggering the alarm, Georgică must follow these rules: All safes are open at second $0$. From each safe $i$, one can take an amount of money equal to $b[i]$. Each safe $i$ will close the moment the money is taken from it. It will reopen exactly $t[i]$ seconds later. Georgică can take money from as many safes as he wants in one second, provided they are open. For example, if Georgică takes money from safe $i$ at second $T$, it will close and reopen at second $T + t[i]$. To ensure that he is a good burglar, Georgică needs to answer $Q$ questions of the type: What is the minimum time in which you can obtain an amount of money greater than or equal to $X$? Help Georgică become a professional burglar by answering these questions!

## Input data

The input file `spargere.in` contains on the first line the number $N$. On the next $N$ lines, there are two natural numbers $b[i]$ and $t[i]$, having the meaning specified in the statement.
On the following line, it contains the natural number $Q$, and on the next $Q$ lines there is a number $X$, representing a question posed to Georgică.

## Output data

The output file `spargere.out` will contain $Q$ lines, each line $i$ containing a single number, representing the answer to question $i$.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq b[i], t[i] \leq 1000$

$1 \leq Q \leq 1000$

$1 \leq X \leq 1000000000$

The seconds are numbered starting from second $0$.

## Example

`spargere.in`
```
2
2 1
3 2
2
11
0
```

`spargere.out`
```
2
1
```

## Explanation

At second $0$, money will be taken from both safes. In total, we will have $5$ money. The first safe will reopen at second $1$, and the second safe at second $2$. At second $1$, we will take money again from the first safe. In total, we will have $7$ money. It will reopen again at second $2$. At second $2$, we will take money from both safes. In total, we will have $12$ money. So, in two seconds, we have at least $11$ money.