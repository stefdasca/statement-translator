## Task

Zaharel is a big fan of numbers. Today, he is playing with numbers of $N$ digits written in base $B$. Let $NR = nr_0 \ nr_1 \ \dots \ nr_{N-1}$ be such a number in base $B$ ($nr_0$, $nr_1$, etc., represent the digits of the number $NR$ written from left to right), we define the image of this number as the number $I(NR) = i_0 \ i_1 \ \dots \ i_{N-2}$ with the property $i_p = \min(nr_p, nr_{p+1})$. Having a lot of free time, Zaharel thought of calculating for each possible $N$-digit number (the number can start with 0s) in base $B$ the product of the digits of its image and sum these values. Write a program that relieves Zaharel from these calculations and determines this sum in due time.

## Input data

The first line of the input file `numere.in` will contain the two natural numbers $N$, $B$, separated by a single space.

## Output data

The first line of the output file `numere.out` will contain the sum desired by Zaharel. Since the result can be very large, it is sufficient to print the remainder when the result is divided by $666013$.

## Constraints

$2 \leq N \leq 20000$

$2 \leq B \leq 1000$

## Example

`nr.in` `nr.out` 
```
2 4
14
```

## Explanation

$NR = 00$, $I(NR) = 0$ adds $0$

$NR = 01$, $I(NR) = 0$ adds $0$

$NR = 02$, $I(NR) = 0$ adds $0$

$NR = 03$, $I(NR) = 0$ adds $0$

$NR = 10$, $I(NR) = 0$ adds $0$

$NR = 11$, $I(NR) = 1$ adds $1$

$NR = 12$, $I(NR) = 1$ adds $1$

$NR = 13$, $I(NR) = 1$ adds $1$

$NR = 20$, $I(NR) = 0$ adds $0$

$NR = 21$, $I(NR) = 1$ adds $1$

$NR = 22$, $I(NR) = 2$ adds $2$

$NR = 23$, $I(NR) = 2$ adds $2$

$NR = 30$, $I(NR) = 0$ adds $0$

$NR = 31$, $I(NR) = 1$ adds $1$

$NR = 32$, $I(NR) = 2$ adds $2$

$NR = 33$, $I(NR) = 3$ adds $3$