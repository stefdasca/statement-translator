# Task

Using the information from the statistics department, determine the number of products and the two products within each offer.

# Input data

The first line of the input file `promo.in` contains the integers $M$ and $K$, separated by a space. The next $K$ lines contain $2$ integers $A$ and $B$, separated by a space, indicating that the offer with number $A$ and the offer with number $B$ have a product in common.

# Output data

The first line of the output file `promo.out` should contain the integer $N$, representing the number of products. The next $M$ lines must contain $2$ integers, separated by a space. The $i$-th line among these $M$ lines will contain the numbers of the products that form the $i$-th offer.

# Constraints and clarifications

* $1 \leq M \leq 2 \ 007$
* $0 \leq K \leq 100 \ 000$
* The determined number of products must be at most equal to $2 \cdot M$.
* The existence of at least one solution is guaranteed. If there are multiple solutions, you can display any of them.

# Example

`promo.in`
```
11 7
1 4
4 7
7 1
2 5
5 8
8 2
10 11
```

`promo.out`
```
17
1 2
3 4
5 6
1 7
3 8
9 10
1 11
3 12
13 14
15 16
15 17
