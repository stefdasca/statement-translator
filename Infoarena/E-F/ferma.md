# The Farm

The tests for this problem are not well-constructed enough to correctly distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Zaharel visited his grandparents' countryside farm with Eugenia. The grandparents' farm is circular in shape, and they have $N$ chickens. The farm is divided into $N$ sectors, numbered from $1$ to $N$, such that any two sectors with consecutive numbers are adjacent (next to each other). Additionally, the first and last sectors are adjacent. Each sector contains one chicken, which lays eggs every day. The grandparents know the productivity of each chicken, which is a number representing the difference between the chicken's consumption and its production. Zaharel and Eugenia collect eggs from the chickens $K$ times a day as follows: each time, they choose a sequence (that is, an array of adjacent sectors) consisting of at least one sector, containing only chickens from which no eggs have been taken that day.

## Task

Knowing the productivity of each chicken and the number of collections in a day, help Zaharel and Eugenia collect eggs so that the sum of the productivities of the chickens from which they collect eggs is maximized.

## Input data

The first line of the input file `ferma.in` contains the natural numbers $N$ and $K$. The next line contains $N$ integers representing the productivity of each chicken.

## Output data

The first line of the output file `ferma.out` will contain the maximum possible sum of the productivities of the chickens from which eggs are collected.

## Constraints and clarifications

$2 \leq N$  
$1 \leq K \leq 1\ 000$  
The productivity of each chicken is an integer in the range $[-100\ 000, 100\ 000]$  
If the maximum possible sum of the productivities is a negative number, $0$ will be printed (it is preferable not to collect any eggs)

## Example

`ferma.in`  
8 2  
2 -6 4 3 -7 -9 10 -1  

`ferma.out`  
18

Please double-check for any potential grammar or syntax errors and correct them according to English language rules before finalizing your translation.