La ora de sport elevii doresc să joace volei. Sunt exact $N$ fete și $N$ băieți și se dorește formarea a două echipe, o echipă formată numai din fete, iar cealaltă numai din băieți. Inițial, elevii au o poziție fixată pe teren. Ei pot fi reprezentați ca $2 \cdot N$ puncte de coordonate întregi în plan. Pentru a putea începe jocul, profesorul de sport trebuie să traseze un fileu (o dreaptă) între echipa băieților și echipa fetelor, astfel încât cele două echipe să se afle de o parte și de alta a fileului. Cum trasarea unui fileu între cele două echipe poate să nu fie posibilă conform așezării inițiale, trebuie să fie efectuate unele schimbări. Astfel, profesorul poate alege la un moment dat o singură fată și un singur băiat, situați la distanța maxim $D$ și să le interschimbe pozițiile (fata va trece în locul băiatului, iar băiatul în locul fetei).

# Task

Determine the minimum number of moves the sports teacher must make to place a net such that it is possible to start the game, as well as the moves made.

# Input data

The input file `volei.in` contains the following:
- The first line contains $N$, the number of girls, which is equal to the number of boys.
- The second line contains the non-zero natural number $D$, with the meaning from the statement.
- Each of the following $2 \cdot N$ lines will contain a triplet of the form $x \\ y \\ \text{tip}$, where $x \\ y$ are the initial coordinates of a student (abscissa, ordinate), and $\text{tip}$ is the character `B` if the corresponding student is a boy or `F` if it is a girl.

# Output data

The output file `volei.out` will contain:
- The first line contains a natural number nrmin representing the minimum number of moves that need to be made.
- The following nrmin lines will display the moves made, one move per line, in the order they were made. A move is described in the form $x1 \\ y1 \\ x2 \\ y2$, with the meaning that the students located at positions $(x1, y1)$ and $(x2, y2)$ will be swapped.

# Constraints and clarifications

* $2 \leq N \leq 7$
* $1 \leq D \leq 30\ 000$
* Coordinates are integers in the interval $[-10\ 000, 10\ 000]$
* There will not be $3$ collinear positions.
* There will not be two people in the same position.
* The distance between points $(x1, y1)$ and $(x2, y2)$ is $\sqrt{(x1 - x2) ^ 2 + (y1 - y2) ^ 2}$.
* If there are multiple possible solutions, display any of them.
* $40\%$ of the score will be awarded per test if the number of moves is correct, and $100\%$ of the score if both the number of moves and the moves made are correct.
* For $50\%$ of the tests, $D$ is larger than the maximum distances between any two points.

# Example

`volei.in`
```
3
4
-2 4 B
-1 3 F
-1 -2 B
1 5 F
3 3 F
6 6 B
```

`volei.out`
```
2
-2 4 -1 3
-1 3 3 3
```

## Explanation

The boy at position $(-2, 4)$ is swapped with the girl at position $(-1, 3)$. Then the boy at position $(-1, 3)$ is swapped with the girl at position $(3, 3)$.
~[volei.png|align=center]