## T-Shirts

Gigel has $N$ T-shirts, each T-shirt having a known number of dots printed as a pattern. Ionel, after looking at the T-shirts for a bit, asks Gigel to select a number of $K$ T-shirts out of the $N$ such that the total number of dots is divisible by $P$. Being picky by nature, Gigel chooses those T-shirts that together have the maximum number of dots and also satisfy the required property. For $M$ requests from Ionel in the specified format, determine the maximum number of dots divisible by $P$ following the selection of exactly $K$ T-shirts.

## Input data

The first line of the input file `tricouri.in` will contain numbers $N$ and $M$, the number of T-shirts, and the number of requests from Ionel, respectively. The second line contains $N$ nonzero natural numbers, separated by a space, representing the number of dots on each T-shirt. The next $M$ lines until the end of the file contain pairs of the form $(K, P)$, representing a request from Ionel.

## Output data

For each request of the form $(K, P)$ from Ionel in the input file, print to the output file `tricouri.out` the maximum number of dots obtained by selecting exactly $K$ T-shirts out of the $N$, which in addition is divisible by $P$. If there is no possible selection, print $-1$ on the corresponding line.

## Constraints and clarifications

$3 \leq N \leq 300\text{ }000$  
$3 \leq M \leq 100$  
For each request from Ionel, $1 \leq K \leq 5$  
$2 \leq P \leq 20$  
The number of dots on each T-shirt is a natural number between $1$ and $1\text{ }000\text{ }000$

## Example

`tricouri.in`  
$7$ $3$  
$5$ $7$ $3$ $4$ $1$ $4$ $8$  
$3$ $5$  
$1$ $10$  
$2$ $4$  

`tricouri.out`  
$20$  
$-1$  
$12$  

## Explanation

For the first request, Gigel will choose the T-shirts with $5$, $7$, and $8$ dots, obtaining a total of $20$ dots, which is divisible by $5$. There is no other possible way to choose exactly $3$ T-shirts that have a total number of dots divisible by $5$ and greater than $20$. For the second request, there is no solution (there is no T-shirt that has a number of dots divisible by $10$). For the last request, Gigel will choose T-shirts with $5$ and $7$ dots, or T-shirts with $4$ and $8$ dots, both cases obtaining a total of $12$ dots.