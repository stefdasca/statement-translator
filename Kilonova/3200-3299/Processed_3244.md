Tuti is a student passionate about physics, and recently he discovered a great fascination for water simulations. Instead of doing his computer science homework, he spent entire hours developing a water simulator. Professor Nea Cais is not at all pleased with this focus, insisting that Tuti should concentrate on his computer science assignments.

Nea Cais proposed to Tuti to solve the problem as efficiently as possible since he is not working otherwise. Being glad to escape Nea Cais's nagging, he accepted.

The water simulator consists of several parts. One of them involves the program determining which molecules are around a given water molecule.

# Task

In the simulator, $N$ molecules are given, indexed from $1$ to $N$ in the order they are received, with integer coordinates $(x, y)$ in a $5 \ 000$ by $5 \ 000$ grid. These are circles with a radius of $0.5$ and they do not intersect.

In practice, Tuti must answer $Q$ questions of $2$ types:
- Operation 1: move a molecule of index $X$ from its initial position $(x, y)$ to another $(z, t)$;
- Operation 2: determine how many molecules are at a maximum distance of 5 from the molecule with index $X$ and what their indices are (the distance is considered from the centers of the molecules).

# Input data:

The first line of the file `watersimu.in` will contain $N$ followed by $Q$. Following this, there will be $N$ lines with pairs $(x_i, y_i)$ representing the position on the grid of the molecule with index $i$.
After this, there will be $Q$ lines with the value 1 or 2 representing the operation:
- If the value is 1, there will also be an $X$ (the index of the molecule) and a $(z, t)$ being the location where it moves;
- If the value is 2, there will also be an $X$ (the index of the molecule).

# Output data:

For each operation of type 2, print on a line of the file `watersimu.out` the number of molecules at a maximum distance of $5$ from molecule $X$ and their indices. The indices should be printed in ascending order.

# Constraints and clarifications
- $1 \leq N, Q \leq 200 \ 000$;
- The tests are generated randomly;
- The molecules do not intersect;
- The distance between 2 molecules is the distance between their centers.
- The coordinates of the centers are natural numbers between $1$ and $5 \ 000$;
- For $50$ points, $n \leq 500$.

# Example

`watersimu.in`
```
6 4
0 0
0 6
3 0
0 30
30 0
5 0
2 4
2 3
1 1 3 3
2 1

```

`watersimu.out`
```
0
2 1 6
3 2 3 6
