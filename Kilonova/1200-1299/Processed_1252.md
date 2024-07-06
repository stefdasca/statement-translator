```markdown
The astronomical research station ONI-2006 has the shape of a cube with a side length of \( N \) units. Each of the 6 faces of the station is divided into \( N \times N \) squares with unit sides. The cosmonauts responsible for the station's maintenance can move on the surface of the cube, using special rails placed in some of the unit squares, to perform various repairs. Some unit squares with rails contain traps for entering the interior of the station. Due to harmful cosmic radiation, cosmonauts need to spend as little time as possible outside the station, so after finishing a repair, they must return to the interior of the station using the nearest access trap. The cosmonaut is initially in a square provided with rails. They can move from one square with rails to another adjacent square (horizontally or vertically) that also has rails. The cosmonaut can also move from one face of the cube to an adjacent face, crossing the common edge. The faces of the cube are described according to the figure below.
\\
~[cub.JPG|align=right|width=auto]
* Face 1: \(ABCD\) - element \((1,1)\) in \(A\) and element \((N,N)\) in \(C\)
* Face 2: \(DCC’D’\) - element \((1,1)\) in \(D\) and element \((N,N)\) in \(C’\)
* Face 3: \(B’A’D’C’\) - element \((1,1)\) in \(B’\) and element \((N,N)\) in \(D’\)
* Face 4: \(BAA’B’\) - element \((1,1)\) in \(B\) and element \((N,N)\) in \(A’\)
* Face 5: \(CBB’C’\) - element \((1,1)\) in \(C\) and element \((N,N)\) in \(B’\)
* Face 6: \(ADD’A’\) - element \((1,1)\) in \(A\) and element \((N,N)\) in \(D’\)

# Task
Write a program that determines the minimum distance from the initial position of the cosmonaut to an access trap, as well as the number of traps at the minimum distance.

# Input data

The input data is read from the file `cub.in`, which has the following structure: The first line contains two natural numbers \(N\) and \(K\), separated by a space, representing the length of the cube's side and the number of access traps, respectively. The second line contains the natural numbers \(F\), \(L\), \(C\), separated by space, designating the unit square on which the cosmonaut initially stands, where \(F \in \{1,2,3,4,5,6\}\) represents the number of a face of the cube, and \(L\) and \(C\) represent the coordinates of the cosmonaut's initial position relative to the corner \((1,1)\) of face number \(F\) (\(L\) – row number, \(C\) – column number). The next \(K\) lines contain 3 natural numbers each, separated by space, representing the coordinates of the \(K\) access traps (face number, row number, and column number). The next \(6 \cdot N\) lines contain the 6 square matrices describing the faces of the cube, with elements from the set \(\{0, 1\}\) (\(0\) – access rail, \(1\) - inaccessible square). The elements of a face are given from \((1,1)\) to \((N,N)\) by rows.

# Output data

The results are written to the file `cub.out`, which has the following structure: The first line will contain the natural number \(LG\), representing the length of the minimum path traveled by the cosmonaut. The length of the path is given by the number of unit squares traversed, including the initial and final positions. The second line will contain the natural number \(T\), representing the number of access traps at the minimum distance from the cosmonaut's initial position.

# Constraints and clarifications

* \(1 \leq N \leq 50\);
* \(1 \leq F \leq 6\);
* \(1 \leq L, C \leq N\);
* The cosmonaut is initially in an accessible position (provided with rails);
* There is at least one accessible trap from the cosmonaut's initial position.

# Example

`cub.in`
```
3 2
2 2 3
5 2 2
3 2 2
1 1 1
1 0 0
1 0 1
0 0 1
0 1 0
0 0 0
1 1 1
1 0 1
1 1 1
1 1 1
1 1 1
1 1 1
1 0 1
1 0 1
1 1 1
1 1 1
1 1 1
1 1 1
```

`cub.out`
```
12
1
```

## Explanation

The illustrated path has a minimum cost of \(12\) and connects the element \((2,3)\) on face \(2\) with the element \((2,2)\) on face \(5\). The other access trap is on face \(3\), in an inaccessible position, so the number of traps at the minimum distance from the starting position is \(1\).
~[cub_exemplu.JPG|align=center|width=auto]
```