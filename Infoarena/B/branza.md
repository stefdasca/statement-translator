# Cheese

The peasant got bored of working in the fields and decided to start a business. In this regard, he opened a cheese factory. In the next $N$ weeks, the price of cheese will fluctuate depending on demand. Fortunately, the peasant knows in advance (it is not known from where) what the prices will be in the coming weeks. He wants to minimize his costs and cover the cheese demand. For each week, he knows the cost $C$ to produce one kg of cheese and the amount $P$ that will be bought. The peasant can produce any amount of cheese in one week. He can store the excess cheese in a warehouse but has to pay $S$ monetary units for each kg of cheese stored for one week. Cheese can be stored for a maximum of $T$ weeks before it spoils. Help the peasant minimize his costs.

## Input data

The first line of the input file `branza.in` contains three integers $N$, $S$ and $T$ with the above meanings. The next $N$ lines each contain two integers $C_i$ and $P_i$, representing the cost to produce one kg of cheese in week $i$ and the amount that will be bought in that week, respectively.

## Output data

The first line of the output file `branza.out` contains a single integer representing the minimum cost necessary for the peasant to satisfy the cheese demand.

## Constraints and clarifications

$1 \leq N, T \leq 100\,000$

$1 \leq S \leq 100$

$1 \leq C_i, P_i \leq 10\,000\,000$

## Example

`branza.in`

```
5 10 3
12 1
21 2
27 4
45 5
52 3
```

`branza.out`

```
488
```

## Explanation

On day 1, the peasant produces 1 kg of cheese with a cost of $12 \cdot 1 = 12$.

On day 2, the peasant produces 2 kg of cheese with a cost of $21 \cdot 2 = 42$.

On day 3, the peasant produces 12 kg of cheese with a cost of $27 \cdot 12 = 324$.

On day 4, the peasant does not produce cheese but pays the storage fee for 8 kg, with a cost of $8 \cdot 10 = 80$.

On day 5, the peasant does not produce cheese but pays the storage fee for 3 kg, with a cost of $3 \cdot 10 = 30$.