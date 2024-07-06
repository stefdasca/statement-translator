Certainly! Here's the translated version of the problem statement in English:

---

Anyone who has watched the Star Trek series remembers the Borg and their cube-shaped spaceship. One of the problems they had to solve before building the ship was the following.

The Borg spaceship has the shape of a rectangular parallelepiped with dimensions \( N \times M \times H \), divided into rooms of dimension \( 1 \times 1 \times 1 \). For the spaceship to function, these rooms must be fitted with \( K \) propulsion engines, with at most one engine per room.

A room can be identified by a triplet \( (a, b, c) \), where \( 1 \leq a \leq N \), \( 1 \leq b \leq M \), \( 1 \leq c \leq H \), representing its coordinates.

A plane of the parallelepiped is a set of rooms of one of the following \( 3 \) types:
\[
\{(a, b, c) \ |\ a \text{ fixed}, \ 1 \leq b \leq M, \ 1 \leq c \leq H \} \text{ -- there are a total of } N \text{ planes of this type};
\]
\[
\{(a, b, c) \ |\ b \text{ fixed}, \ 1 \leq a \leq N, \ 1 \leq c \leq H \} \text{ -- there are a total of } M \text{ planes of this type};
\]
\[
\{(a, b, c) \ |\ c \text{ fixed}, \ 1 \leq a \leq N, \ 1 \leq b \leq M \} \text{ -- there are a total of } H \text{ planes of this type}.
\]

# Task
Find `R`, the number of ways to place the `K` engines so that any plane of the parallelepiped contains at least one room occupied by an engine.

Since the required number can be very large, it is sufficient to find the remainder of `R` divided by `30103`.

# Input data
The input file `borg.in` will contain a single line with the natural numbers `N`, `M`, `H`, and `K` separated by a space.

# Output data
The output file `borg.out` will contain a single line with a single natural number representing the remainder of `R` divided by `30103`.

# Constraints and clarifications
* \( 1 \leq N, M, H \leq 20 \)
* \( 1 \leq K \leq N \times M \times H \)
* `80%` of the tests will have \( K \leq 2000 \)

# Examples

`borg.in`
```
3 1 2 4
```
`borg.out`
```
12
```
`borg.in`
```
3 1 2 2
```
`borg.out`
```
0
```

---