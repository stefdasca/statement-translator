Costel really enjoyed the movie "Star Wars," so he thought about building a *droid* with side length $k$ as follows: He will build 3 platforms of $k \times k$ (one on top of the other), the base of the droid, and on the edges, there will be two "rows" of length $k$ (each consisting of $k$ blocks), representing the "blasters." The platforms and blasters will be connected, but no block will belong to both a platform and a blaster simultaneously.

# Task

Given an integer $n$. Calculate how many numbers $p$ from $1$ to $n$ have the property that a droid can be built using exactly $p$ blocks.

# Input data

The first line of the input file `starwars.in` contains a single natural number, $n$.

# Output data

The first line of the output file `starwars.out` will contain a single integer, the number of numbers from $1$ to $n$ that have the required property.

# Constraints and clarifications

* $1 \leq n \leq 10 ^ 9$
* For $50$ points, $n \leq 100 \ 000$.
* For the other $20$ points, $n \leq 10 \ 000 \ 000$.

# Example

`starwars.in`
```
40
```

`starwars.out`
```
3
```

## Explanation

The $3$ numbers are: $5$, $16$, $33$.