# Ferma2

The crisis has even hit our old friend, farmer Ion. Running out of the money needed for farm maintenance, he decided to sell plots over the course of $K$ days. Ion's land is in the shape of an isosceles right triangle with leg $N$, consisting of $1 \times 1$ squares, each having different sale values. Fearing the tax authorities, the farmer decided to sell exactly one plot per day. In order not to attract the attention of the neighbors, the plot must be along one of the sides of the current land, as shown in the figure below: Help our friend achieve the maximum possible profit from selling the plots without the tax authorities or envious neighbors detecting him.

## Input data

The input file `ferma2.in` will contain on the first line the numbers $N$ and $K$. The following $N$ lines will contain the garden's configuration: the $(i + 1)$-th line will contain $i$ numbers each representing the value of the respective plot.

## Output data

The output file `ferma2.out` will print on the first line the maximum profit Ion can obtain.

## Constraints

$1 \leq N \leq 1000$

$0 \leq K \leq N$

$0 \leq$ profit obtained by Ion for a $1 \times 1$ square $\leq 100$

## Example

`ferma2.in`

```
5 3
82
55 3
67 46 52
62 20 54 85
66 32 40 78 52
```

`ferma2.out`

```
702
```

## Explanation

On the first day, Ion sells the plots with the values: $82$ $55$ $67$ $62$ $66$. On the second day, he sells the plots: $3$ $52$ $85$ $52$. On the last day, he sells: $46$ $54$ $78$. The total profit obtained is $82 + 55 + 67 + 62 + 66 + 3 + 52 + 85 + 52 + 46 + 54 + 78 = 702$.