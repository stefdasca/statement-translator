The Institute for Insect Research has discovered that if ants are placed on a metal bar, they have a well-defined behavior according to the following rules:

1. As soon as it is placed on the bar, it starts moving in the direction it is oriented, with a constant speed of $1$ cm/s. The ant does not stop as long as it is on the metal bar even if it collides with another ant.
2. If on the way it does not encounter another ant, it will continue to move until it falls off the bar.
3. When two ants meet, they both instantly change direction of movement.

# Task

Knowing that exactly $N$ ants are placed on a metal bar of length $L$ cm in known positions and with known initial directions of movement, write a program that calculates the number of seconds after which the last ant falls off the bar from the initial moment. All ants start moving simultaneously.

# Input data

The input file `furnici.in` contains on the first line two natural numbers $L$ and $N$ separated by a space. Then follow $N$ lines each with $2$ values: $poz_i$ and $sens_i$ separated by a space, where $poz_i$ is a natural number representing the coordinate where ant $i$ is initially, and $sens_i$ is a character from the set $\{ 'S', 'D' \}$ indicating the initial direction of movement the ant $i$ has ($S$ for left and $D$ for right).

# Output data

The output file `furnici.out` will contain a single number representing the time when the last ant falls.

# Constraints and clarifications

* $1 < L < 10 \ 000 \ 000$
* $0 < N < 100 \ 000$
* $0 \leq poz_i \leq L$

# Example

`furnici.in`
```
10 3 
4 D
8 S
1 S
```

`furnici.out`
```
8
```

~[Poza1.png|align=right]

# Explanation

The bar is $10$ cm long and $3$ ants are placed on the bar at distances of $4$, $8$, and $1$ from the left end of the bar, with the following directions of movement: right, left, and left.

The first two ants will meet after $2$ seconds at coordinate point $6$ and will change their direction of movement.

After changing direction, the second ant will travel another $4$ cm to the right and will fall, while the first ant will continue $6$ cm to the left, until it falls. During this time, the third ant will have fallen off the bar after $1$ second.

No ants will remain on the bar after $8$ seconds.