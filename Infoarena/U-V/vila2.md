## Vila 2

Along the Autostrada Soarelui, $n$ beautiful villas were built, numbered in order from $1$ to $n$. In each villa lives a solarian. The administration has concluded that solarians get along better with each other when their ages are closer, so they are interested in finding the maximum age difference between any two neighbors.

## Task

Knowing the age of each solarian, find the maximum age difference between two neighbors. Solarians understand neighbors as two inhabitants for whom the modulus difference between their villa numbers does not exceed the number $k$. 

## Input data

The first line of the input file `vila2.in` contains the numbers $n$ and $k$, separated by a single space. The next $n$ lines contain $n$ integers, representing, in order, the ages of the solarians. 

## Output data

The first line of the file `vila2.out` will contain the maximum difference found. 

## Constraints

$2 \leq n \leq 100\,000$ 

$1 \leq k \leq n/2$ 

A solarian lives for at most $30\,000$ years 

## Example

`vila2.in`

```
6 2
5
9
4
7
4
1
```

`vila2.out`

```
6
```