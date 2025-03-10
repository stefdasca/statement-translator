
~[img1.png|align=right]

Vlad and Andrei want to decorate the garden in the spirit of Halloween and they have a bunch of carved pumpkins at their disposal! They would like to create a wall of $N-1$ pumpkin towers, and for the stability of the arrangement, they have $N$ wooden poles with distinct heights from $1$ to $N$.

The pumpkins are placed between the poles, one on top of the other, forming towers. A pumpkin tower of height $D$ is stable if and only if on both its left and right (but not necessarily immediately adjacent) there is at least one pole of height greater than or equal to $D$. Because they ordered a perhaps too large number of pumpkins, Vlad and Andrei would like to make the arrangement using as many pumpkins as possible, using the rest to make pies.

Unfortunately, they must also follow the next rule when arranging the poles: the number of pairs of different poles for which the taller pole is placed before the shorter pole must be exactly $K$. Such a situation is called an _inversion_.

# Task
For $50\%$ of the score, determine only the maximum number of pumpkins that can be used so that the arrangement of the $N$ poles has exactly $K$ inversions. Additionally, for maximum points, determine and display such an arrangement of the poles.

# Input data

The input contains a single line containing 2 integers representing $N$ and $K$.

# Output data

Print on the first line a single integer representing the maximum number of pumpkins that can be used in the arrangement.

For complete scoring, on the second line, print $N$ space-separated numbers representing an arrangement model of the poles with $K$ inversions that maximizes the number of pumpkins.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $0 \leq K \leq \frac{N\times (N-1)}{2}$
* If there are multiple arrangements that correspond, any one can be shown.

| #  | Score  | Constraints                                                   |
|----|--------|---------------------------------------------------------------|
| 1  | 14     | $ K = N - 2 $                                                 |
| 2  | 15     | $ N - 2 \leq K \leq \frac{N \times (N-1)}{2} - (N - 2)$       |
| 3  | 19     | $ 2 \leq N \leq 6 $                                           |
| 4  | 12     | $ 2 \leq N \leq 100 $                                         |
| 5  | 17     | $ 2 \leq N \leq 1\ 000 $                                      |
| 6  | 23     | No additional constraints.                                    |

# Example 1

`stdin`
```
3 1
```

`stdout`
```
4
2 1 3
```

# Example 2

`stdin`
```
3 0
```

`stdout`
```
3
1 2 3
```

# Example 3

`stdin`
```
3 3
```

`stdout`
```
4
3 2 1
```
## Explanations for examples

~[DovleciExplicatie.png]
