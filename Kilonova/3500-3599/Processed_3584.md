**Orzeni** is a village in the commune of **Holboca** in **Iași** County, **Moldova**, **Romania**. - [wikipedia](https://ro.wikipedia.org/wiki/Orzeni,_Ia%C8%99i)

~[orzeni.png|align=center|width=30em]

**Marcel**, an informatics olympiad participant (honorable mention at **OMI**) and proud citizen of Orzeni, is preparing once again this year for the olympiad, specifically the **OJI**. As the local mindset gives him quite a headache: **"People need to do some fieldwork too, we should leave those buttons alone as they harm your eyes" - Marcel's mother**, he finds himself once again having chores to do, namely he has to go to the store to buy sausages and beans.

# Task

In Orzeni, there are exactly $N$ stores, with the $i$-th store having a value $a_i$. The boy receives a list of $K$ products, which he conveniently numbers from $1$ to $K$ and he is required to purchase them in ascending order. A store $i$ has the product $p$ if and only if $p | a_i$, or put more simply, if $a_i$ is exactly divisible by $p$.

Knowing that the distance between two stores $i$ and $j$ is $|i - j|$ and that Marcel can start from any store, calculate the minimum distance he must travel so that he purchases all $K$ products.

# Input data

The first line contains 2 numbers, $N$ and $K$. The next line contains $N$ natural numbers, separated by a space.

# Output data

The first line will print the minimum distance traveled by Marcel, and if he cannot purchase all the products, it will print $-1$.

# Constraints and clarifications

* The distance from his house to the first store visited is not taken into account.
* $1 \leq N,K,a_i \leq 10^5$.

| # | Score | Constraints |
| - | ----- | ------------ |
| 1 | 5 | $N,K \leq 100$ |
| 2 | 20 | $N,K \leq 1 \ \ 000$ |
| 3 | 30 | $K,a_i \leq 100$ |
| 4 | 45 | No other constraints |

# Example 1

`orzeni.in`
```
6 5
45 68 28 43 79 55 
```

`orzeni.out`
```
3
```

## Explanation

The path traveled by Marcel is $2 \rightarrow 2 \rightarrow 1 \rightarrow 2 \rightarrow 1$.

# Example 2

`orzeni.in`
```
11 10
28 39 50 66 22 14 34 29 65 24 3 
```

`orzeni.out`
```
-1
```

## Explanation

The product with number $9$ cannot be found in any store.