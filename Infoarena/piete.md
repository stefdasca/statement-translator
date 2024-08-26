# Markets

In a country, there are $N$ cities, each having a market where people can buy and sell items. There are $M$ types of items that are traded, and each market has its own buying and selling prices for any of the $M$ items, not necessarily different from those in other markets. Being smart, Claudia realized that she can make a profit by purchasing items in one city and selling them in another city. She plans to increase her savings by buying and selling products in the markets of the country and reaching a final amount she aims to surpass. Due to the strict system imposed by the tyrant king, trade in the country is discouraged. The king has decreed that no one is allowed to travel from one city to another with more than one item of the same type and forces all merchants entering a city to sell all items brought before making any new purchases. Also, for any transportation of items from one city to another, the respective merchant will receive a black mark in the king's ledger.

## Task

Write a program to help Claudia reach at least the desired final amount, with a minimum number of black marks recorded in the king's ledger.

## Input data

The first line of the `piete.in` file contains four non-zero natural numbers $N$, $M$, $S$, $F$ separated by spaces, with the following meanings:
- $N$ – the number of cities;
- $M$ – the number of types of items in each market;
- $S$ – an amount of money representing Claudia's initial savings;
- $F$ - an amount of money representing the desired final amount. 

On the following $N$ lines, there are $M$ numbers separated by spaces: the $j$-th number on line $i$ represents the buying/selling price of item $j$ in market $i$. 

## Output data

The first line of the `piete.out` file contains the minimum number of black marks that Claudia will receive if she manages to reach at least the amount $F$. If she has no way to reach the amount $F$ then $-1$ will be printed.

## Constraints and clarifications

$1 \leq N \leq 10$

$1 \leq M \leq 10$

$1 \leq S \leq F \leq 100$

$0 \leq p[i, j] \leq 100$

$p[i, j]$ = the price of item $j$ at market $i$

There is a direct path between any two cities

In any market, the selling price of an item is the same as its purchase price

## Example

`piete.in`

```
3 4 10 20
5 1 16 4
4 2 13 3
6 3 20 5
```

`piete.out`

```
2
```

## Explanation

Buy items $1$, $2$, and $4$ from city $1$ (remaining with $0$ money). Go to city $3$ and sell them. Now has $14$ money and one black mark. Buy item $3$ from city $2$ (1 money left). Go to city $3$ and sell it. Now has $21$ money and $2$ black marks. She achieved the desired amount and the number of black marks is minimal.

`piete.in`

```
2 3 3 6
4 7 8
6 5 9
```

`piete.out`

```
-1
```

## Explanation

Cannot buy any item hence cannot make a profit.