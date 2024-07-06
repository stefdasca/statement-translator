~[insula.png|align=right]
On the shore of the island Mauritius there are $N$ localities, numbered from $1$ to $N$, considered points of great attraction for tourists. These are connected through a railway network with double-track that connects the localities $1$ to $2$, $2$ to $3$, $\ldots$, $N - 1$ to $N$ and $N$ to $1$, thus allowing two circuits. The first circuit involves visiting localities $1$, $2$, $\ldots$, $N$, $1$, in this order, and the second circuit involves visiting localities $1$, $N$, $N - 1$, $\ldots$, $2$, $1$. In each locality, there are agencies of all $M$ tourism operators, numbered from $1$ to $M$.
A travel ticket can only be purchased from the locality where the traveler is located and allows travel from that locality to the next locality in the circuit. To build customer loyalty, tourism operators use the following rule for ticket prices: if a traveler has arrived at a station with a ticket purchased from a certain tourism operator and continues their journey to the next destination with a ticket bought from another tourism operator, then the new ticket will have its price doubled.
Ștefan is on vacation on the island in locality $1$ and has just won a prize offered by tourism operator number $1$, for a trip with $N$ travel tickets on the island of Mauritius.
He starts from the locality he is in and then travels by train the entire circuit, so that with the last ticket purchased he returns to locality $1$, from where he started. The same tourism operator offers him, for a fee, the first travel ticket. Ștefan will study all offers and if necessary he can refuse this first ticket to purchase it from another tourism operator, even if its price will be doubled (because he changed the operator).

# Task

Knowing the prices of travel tickets, set by each tourism operator, determine the minimum sum with which Ștefan can purchase the $N$ tickets necessary for his trip.

# Input data

The input file `insula.in` contains:

* the first line contains two natural numbers $N$ and $M$, separated by a space with the significance given in the statement;
* on the next $M$ lines, $N$ natural numbers $p_{i1}$, $p_{i2}$, $\ldots$, $p_{in}$, separated by spaces. The values in line $i + 1$ represent, in order, the prices set by the operator numbered $i$ for purchasing travel tickets between the localities $1$ and $2$, $2$ and $3$, $\ldots$, $N - 1$ and $N$, respectively $N$ and $1$.

# Output data

The output file `insula.out` will contain on the first line a single natural number that represents the minimum sum with which Ștefan can purchase the $N$ tickets for his trip.

# Constraints and clarifications

* $3 \leq N < 300$, $N$ odd number;
* $1 \leq M < 300$
* ticket prices are non-zero natural numbers with at most two digits each;
* for $40\%$ of the score, $N < 10$

# Example

`insula.in`
```
3 2
10 9 3
2 8 5
```

`insula.out`
```
16
```

## Explanation

In the circuit there are $3$ localities and $2$ tourism operators.
Operator $1$ has the following prices: for travel between localities $1$ and $2$ the ticket costs $10$, between localities $2$ and $3$ the ticket costs $9$, and between localities $3$ and $1$, the ticket costs $3$.
Operator $2$ has the following prices: for travel between localities $1$ and $2$ the ticket costs $2$, between localities $2$ and $3$ the ticket costs $8$, and between localities $3$ and $1$, the ticket costs $5$. A journey with $3$ tickets can be: $1 \rightarrow 3$ price $3$, $3 \rightarrow 2$ price $9$, $2 \rightarrow 1$ with price $2$ from operator $2$ (the price doubles)
Total minimum cost $3 + 9 + 2 \cdot 2 = 16