# Stamps

As you all know, Adriana is a great stamp collector. Every day she goes to the shop on her street to grow her collection. One day, the shopkeeper (none other than Balaurul Arhirel) decided to surprise her. He took out some very valuable stamps from an old cupboard, on which natural numbers were written with gold and silver thread. Knowing that the little girl does not have much money, Balaurul told her the following: "I can divide the stamps into $M$ intervals of the form $[1, \dots, m_i]$. You can take from any interval a single subarray of at most $K$ elements. Of course, if you choose a subarray from interval $i$ you will pay a certain amount..." Adriana thought it would be nice to number all $N$ pages of her album with such stamps. Being a little girl with a sweet tooth, she said to herself: "I really want to eat an ice cream with the money I have on me, but I don't know if I will have enough to pay for the stamps. What should I do?"

## Task

Knowing the $M$ intervals, as well as their costs, help Adriana buy the necessary stamps for numbering the album, paying the smallest possible sum.

## Input data

The first line of the file `timbre.in` contains $N$, $M$, and $K$. $N$ represents the number of pages in the album, $M$ represents the number of intervals, and $K$ the maximum length of a subarray. The next $M$ lines contain two numbers separated by a space, $m_i$ and $c_i$, where $m_i$ represents the upper bound of interval $i$, and $c_i$ its cost.

## Output data

The first line of the file `timbre.out` will contain $Smin$, representing the minimum sum Adriana has to pay to buy the stamps necessary for numbering the album.

## Restrictions and clarifications

$0 < N < 1001$

$0 < M < 10001$

$0 < K < 1001$

$0 < m_i < 100\,000$

$0 < c_i < 10\,000$

To number all $N$ pages of the album, Adriana needs stamps with numbers from $1$ to $N$.

## Example

`timbre.in`
```
4 3 2
5 3
2 1
6 2
```

`timbre.out`
```
3
```

## Explanation

We take subarray ${1, 2}$ from the second interval and subarray ${3, 4}$ from the third interval. This way, we obtain the minimum cost $3$.