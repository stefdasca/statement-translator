> \- Ia, eu fac ce fac de mult,
> Iarna viscolu-l ascult,
> Crengile-mi rupându-le,
> Apele-astupându-le,
> Troienind cărările
> și gonind cântările
> Mihai Eminescu, Revedere

# Task

El Capoc, after the harsh winter of '20-21, was left without leaves. Ashamed, he retreated to the countryside, where he will earn his living by growing peppers. Fortunately for him, the crop in his first year was very bountiful, amounting to $n$ peppers, with the weight of the $i$-th pepper known as $a_i$ grams.

To be able to pay the gas bill for the upcoming winter, El Capoc found $k$ clients who want to buy peppers. Therefore, the $n$ harvested peppers will be divided into $k$ baskets, with the intention of giving each client one basket of peppers.

To avoid upsetting his clients, **each basket must contain at least one pepper**. Due to the unusual method of transporting the baskets using carrier pigeons, the baskets need to be as balanced as possible. The *imbalance* of a basket is equal to the weight difference between the largest and smallest pepper in that basket. The *total imbalance* is equal to the sum of the imbalances of the $k$ baskets.

El Capoc wants to find out the minimum *total imbalance* he can achieve by distributing the $n$ peppers into $k$ baskets.

# Input data

The first line of the input file `ardei.in` will contain two numbers $n$ and $k$ ($1 \le k \le n \le 500\ 000$) — the number of peppers and the number of clients, respectively.

The second line of the input file will contain $n$ numbers, the weights of the peppers ($1 \le a_1, a_2, a_3, \ldots, a_n \le 1\ 000\ 000\ 000$).

# Output data

The first line of the output file `ardei.out` should contain the minimum *total imbalance*.

# Constraints and clarifications
|#|Points|Constraints                            |
|-|-------|--------------------------------------|
|1| 10    | $k=1$                                |
|2| 15    | $k=2, n \le 3\ 000$                  |
|3| 20    | $k=2$                                |
|4| 15    | $n \le 3\ 000$                       |
|5| 20    | $n \le 100\ 000$                     |
|6| 20    | No additional constraints            |

# Example 1

`ardei.in`

```
8 3
10 7 2 9 9 4 6 3
```

`ardei.out`
```
4
```

## Explanation 

An optimal distribution would be for the first basket to contain peppers with weights $[10,9,9]$, the second basket to contain peppers with weights $[7,6]$, and the third basket to contain peppers with weights $[2,4,3]$. The *total imbalance* is equal to $(10-9)+(7-6)+(4-2)=4$.