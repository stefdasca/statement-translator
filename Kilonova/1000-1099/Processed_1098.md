In the 23rd century, humans began to traverse intergalactic space. The ships they travel with are truly wonders of technology, using a very exotic type of fuel.

This type of fuel can be obtained by combining exactly two reactants, one stable and one unstable.

Each reactant is assigned a value in the form of a non-zero natural number. A reactant is said to be stable if its value is a prime number and unstable if its value is not a prime number.

However, not all types of fuel are equally valuable. As you might expect, the price of a type of fuel is equal to the sum of the values of the reactants that compose it.

# Task

Knowing that there are $N$ reactants on the intergalactic market, answer $T$ questions of the type: what is the price of the $K$-th cheapest type of fuel that can be created using only the reactants available on the market.

# Input data

The file `intergalactic.in` will contain on the first line the numbers $N$ and $T$, representing the number of reactants on the market and the number of questions. The second line will contain $N$ numbers separated by a space, representing the values of the $N$ reactants. On the following $T$ lines there will be a single number $K$ with the significance given in the description.

# Output data

The file `intergalactic.out` will contain $T$ lines, each line containing a single number representing the answer to question $i$.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq N \leq 200\ 000$
* $1 \leq K \leq 10^9$
* It will always be possible to create at least $K$ types of fuel.
* There will be no 2 reactants with the same value.
* There will be at least one stable reactant and one unstable reactant on the market.
* The value of a reactant is less than or equal to $2\ 000\ 000$.
* Two types of fuel with the same price are different if they come from different pairs of reactants.
* For tests worth $7$ points: There is either a single stable reactant or a single unstable reactant on the market.
* For other tests worth $11$ points: $K \leq 100$
* For other tests worth $21$ points: $N \leq 1\ 000$
* For other tests worth $28$ points: $N \leq 30\ 000$
* For other tests worth $33$ points: there are no additional restrictions

# Example

`intergalactic.in`
```
8 3
3 7 2 1 11 8 10 4
15
7
11
```

`intergalactic.out`
```
19
11
13
```

## Explanation

Unstable reactants are: $1$, $4$, $8$, $10$
Stable reactants are: $2$, $3$, $7$, $11$

The ordered values of the types of fuel that can be created are:

$3$, $4$, $6$, $7$, $8$, $10$, $11$, $11$, $12$, $12$, $13$, $15$, $15$, $17$, $19$, $21$

The $15$-th cheapest fuel has a value of $19$.

The $7$-th cheapest fuel has a value of $11$.

The $11$-th cheapest fuel has a value of $13$.