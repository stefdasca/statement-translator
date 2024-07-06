Here is the translated problem statement in English:

---
Today, all the $n$ kids in the neighborhood want to play basketball. Since there are many of them and they couldn't agree on how to form the teams, they decided to take turns shooting at a single basket. They also set a rule for the game: each one will shoot as long as they score, and each basket counts as one point. The game ends when all the kids have taken their turn, in the agreed order.

# Task

Write a program to determine the number of consecutive kids-players who shot the basket and scored the same number of baskets, as well as the total number of points accumulated by them.

# Input data

The first line of the input file `baschet.in` contains the number $n$. Then, $n$ numbers follow, representing the number of points scored by each player.

# Output data

The first line of the output file `baschet.out` will contain the number of players and the number of accumulated points, separated by a space.

# Constraints and clarifications

* $6 < n < 31$;
* The numbers are natural and strictly less than 41.
* If there are multiple sequences of equal numbers, the first one will be considered.
* Only sequences with at least $2$ kids who achieved the same score are considered.

# Example 1

`baschet.in`
```
10
1 2 9 3 3 3 7 7 7 3
```

`baschet.out`
```
3 9
```

## Explanation

We have the subarray $3 \ 3 \ 3$, of length $3$, of the kids' shots who scored the same number of points. The number of accumulated points is $9$.

