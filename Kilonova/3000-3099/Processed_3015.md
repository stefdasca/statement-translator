The crew of the starship Enterprise has discovered on the planet Mars an area with $b$ military bases that house the Martian combat ships. The crew managed to map the area and divided the planet's map into $n \times m$ zones with side length $1$, arranged in $n$ rows (numbered from top to bottom from $1$ to $n$) and $m$ columns (numbered from left to right from $1$ to $m$). Thus, each zone can be identified by the row and column number it is located in.

In each such zone, there is a Martian base housing a number of ships. The captain of the Enterprise, Jean-Luc Picard, has devised an attack strategy against these military bases. 
The Enterprise can land in a zone where there is no Martian base and can launch a single attack (because after the first attack, the Martian bases will activate their protective shields). In one attack, $2$ laser beams are emitted simultaneously, destroying all Martian ships in the bases located in the direction of these beams, in both senses. The beams are emitted from the center of the zone where the Enterprise has landed and form angles of $45^o$ and $135^o$ with the row on which the Enterprise is located.

~[nave.png|align=center]

# Task

Write a program that, given the configuration of Martian bases, determines the maximum number of Martian ships that the Enterprise can destroy in a single attack, as well as the row and column of the zone where the Enterprise can land to destroy a maximum number of ships. If there are multiple zones where the Enterprise can land conveniently, it should choose the zone for which the row is maximum; if there are multiple zones on the maximum row, it will choose the one for which the column is maximum.

# Input data

The input file `nave.in` contains on the first line three natural numbers $n$, $m$, and $b$, separated by a space, representing the number of rows, the number of columns of the map of the planet Mars, and the number of Martian bases, respectively. On each of the following $b$ lines, a Martian base is described in the form of three natural numbers separated by a space, $lin \ col \ nr$, representing the row and column on which the Martian base is located, and the number of ships located in that Martian base, respectively.

# Output data

The output file `nave.out` will contain on the first line three natural numbers $nr_{max} \ lin_{max} \ col_{max}$, separated by a space, representing the maximum number of Martian ships that the Enterprise can destroy in a single attack, as well as the row and column of the zone where the Enterprise can land to destroy a maximum number of ships. If there are multiple zones where the Enterprise can land conveniently, it should choose the zone for which the row is maximum; if there are multiple zones on the maximum row, it will choose the one for which the column is maximum.

# Constraints and clarifications

* $1 \leq n, m \leq 100$
* $\sqrt{n \cdot m} \leq b \leq \frac{n \cdot m}{2}$
* $1 \leq lin \leq n$; 
* $1 \leq col \leq m$; 
* $1 \leq nr \leq 1 \ 000$;

# Example

`nave.in`
```
5 4 9
1 1 3
1 2 5
2 2 7
2 4 9
3 1 6
3 3 8 
4 1 1 
5 1 4
5 3 2
```

`nave.out`
```
29 4 2
```

## Explanation

The map of the area where the Martian bases are located is:

```
3  5  0  0 
0  7  0  9 
6  0  8  0 
1  0  0  0 
4  0  2  0
```

If the Enterprise lands in the zone located on row $4$ and column $2$, it will destroy a maximum number of ships $(29)$.