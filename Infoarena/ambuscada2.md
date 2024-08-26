# Ambuscada2

$N$ soldiers, numbered from $1$ to $N$, are caught in an ambush. There are $M$ cannon attacks on them. The attacks affect not just one soldier, but a range of soldiers, causing each of them a certain amount of damage. For example, the attack $(3,7,5)$ affects soldiers $3,4,5,6,7$ with $5$ damage. At the beginning, all soldiers have $V$ lives. How many soldiers remain alive after the $M$ attacks?

## Task

## Input data

The input file `ambuscada2.in` contains on the first line the natural numbers $N$, $M$, and $V$ separated by spaces. On the next $M$ lines, there are $3$ natural numbers $i$ $j$ $k$ separated by a space, representing the details of each attack as described above.

## Output data

The output file `ambuscada2.out` will contain a single natural number representing the number of soldiers remaining alive.

## Constraints and clarifications

$2 \leq N \leq 1\ 000\ 000\ 000$

$1 \leq M \leq 100\ 000$

$1 \leq V \leq 1\ 000\ 000\ 000$

In all tests,

$1 \leq i \leq j \leq N$

$1 \leq k \leq V$

For tests worth $30$ points:

$N \leq 100\ 000$

$M \leq 50$

## Example

`ambuscada2.in`

$6 \ 4 \ 10$

$2 \ 5 \ 2$

$1 \ 3 \ 7$

$2 \ 6 \ 3$

$3 \ 5 \ 6$

`ambuscada2.out`

$2$

## Explanation

Initially, all soldiers had $10$ lives.

After the first attack:

$10 \ 8 \ 8 \ 8 \ 8 \ 10$

After the second attack:

$3 \ 1 \ 1 \ 8 \ 8 \ 10$

After the third attack:

$3 \ 0 \ 0 \ 5 \ 5 \ 7$

After the fourth attack:

$3 \ 0 \ 0 \ 0 \ 0 \ 7$

In the end, $2$ soldiers remained alive: the first and the last.