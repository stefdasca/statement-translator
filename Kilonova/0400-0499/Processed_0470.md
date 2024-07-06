Rapunzel, bored with the way her castle looks, wants to make some changes. Thus, she ordered a new mosaic to be placed at the entrance. The palace craftsmen, knowing how indecisive the princess is, decided to come up with as many possible patterns.

The ordered mosaic is a simple one, composed of two overlapping strips of length $N$. To achieve this, the craftsmen have an infinite number of rectangular tiles of variable lengths and widths equal to the width of a strip. Any two tiles of different lengths also have different patterns.

To avoid overloading the mosaic, one strip will contain the same tile pattern. Because materials are expensive, the craftsmen want to use each tile entirely, without exceeding the length of the mosaic.

While working on the mosaic, Prince Flynn also added a condition: the number of tiles used for the first strip and the number of tiles for the second strip must be coprime.

A bit worried about this condition, the craftsmen ask for your help in calculating how many patterns they will present to the princess upon completing the order.

# Task 1

Before starting their work, the craftsmen want to know the lengths of the tiles that could be used in creating the mosaic.

# Task 2

Determine the number of patterns the princess will receive from the craftsmen.

# Input data

The first line contains a number $T$ which can be $1$ or $2$, depending on the task number to be performed. The next line contains a number $N$, which represents the length of the mosaic.

# Output data

For $T = 1$ in the output file, print, separated by a space, all the lengths of the tiles, in ascending order.

For $T = 2$, in the output file, print the number of patterns.

# Constraints and clarifications

* Tiles have any positive natural number length;
* There are an infinite number of tiles of the same length;
* $1 \leq T \leq 2$;
* $q \leq N \leq 2 \ 000 \ 000$;
* For $20$ points, $T = 1$;
* For $30$ points, $T = 2$ and $1 \leq N \leq 500$;
* For $10$ points, $T = 2$, $N \gt 500$ and $N$ is prime;
* For $40$ points, $T = 2$.

# Example 1

`stdin`
```
1
9
```

`stdout`
```
1 3 9
```

## Explanation

A strip of length $9$ can be completed with $9$ tiles of length $1$, $3$ tiles of length $3$, or one tile of length $9$.

# Example 2

`stdin`
```
2
9
```

`stdout`
```
3
```

## Explanation

The three patterns that the princess can achieve contain the tiles with the following lengths:

$1 \ 9$  
$3 \ 9$  
$9 \ 9$

~[mozaic.png|width=10em]

It can be observed that $1 \ 3$ is not a valid pattern, because the number of tiles needed to complete the first strip would be $9$, and the number of tiles needed to complete the second strip would be $3$, the two numbers not being coprime.

Also, the patterns $9 \ 1$ and $9 \ 3$ were not considered, being regarded as the same as the patterns $1 \ 9$ and $3 \ 9$ respectively.

# Example 3

`stdin`
```
2
17
```

`stdout`
```
2
```

## Explanation

The two patterns that the princess can achieve contain the tiles with the following lengths:

$1 \ 17$  
$17 \ 17$

~[mozaic2.png|width=30em]