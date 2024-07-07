
> *Colegiul Național “Frații Buzești�* ~[logos.png|align=right|width=20rem]
> *Centrul de Pregătire pentru Performanță în Informatică*
> **InfoCNFB** - 2nd Edition, Juniors
> December 9, 2023

# Task

We are given two arrays $A$ and $B$, both with $n$ elements, sorted in ascending order. We are also given a number $m$. We want to construct an array $C$ with $m$ elements with the following properties:
* it should be in ascending order;
* there should exist a value $p$ ($1 \leq p < m$), such that the first $p$ elements of $C$ form a subarray in $A$, and the last $m-p$ elements of $C$ form a subarray in $B$;
* considering $D$ as the array with the $m-1$ differences of consecutive elements in $C$ (in absolute value), the maximum value from $D$ should be as large as possible.

# Input data

The file `abrupt.in` contains on the first line the numbers $n$ and $m$, separated by a space. The second line contains $n$ natural numbers, in ascending order, separated by spaces, representing the elements of array $A$. The third line contains $n$ natural numbers, in ascending order, separated by spaces, representing the elements of array $B$.

# Output data

The file `abrupt.out` will contain a single natural number representing the maximum value from array $D$.

# Constraints and clarifications

* $1 \leq n \leq 300\ 000$;
* $2 \leq m \leq 2 \times n$;
* The elements of arrays $A$ and $B$ are natural numbers at most equal to $2\ 000\ 000\ 000$;
* For $20$ points, $n \leq 50$;
* For $40$ points, $n \leq 200$;
* For $60$ points, $n \leq 2\ 000$;

# Example

`abrupt.in`
```
3 4
2 6 7
3 8 9
```

`abrupt.out`
```
5
```

## Explanation

We can form the array $C$ as follows: $2 \ 3 \ 8 \ 9$. The array $D$ would have the values $1 \ 5 \ 1$.
```
