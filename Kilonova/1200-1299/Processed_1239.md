
Localitatea Târgoviște este în plină modernizare. Primăria decide să inventarieze toate clădirile din oraș pentru a renova fațadele acestora. În acest sens analizează harta orașului și constată că toți pereții sunt așezați doar pe direcția Nord Sud sau Est Vest. Pereții vizibili de către turiști sunt doar aceia la care se poate ajunge din exteriorul orașului prin deplasarea pe cele două direcții date, în oricare din cele $4$ sensuri $(N, E, S, V)$. Harta orașului este întocmită pe un caroiaj format din pătrate cu latura $1$. 

# Task

Given the map of the city, determine the length of the visible walls that are to be painted.

# Input data

The input file `pereti.in` contains on the first line the dimensions $m$ (number of rows), $n$ (number of columns) of the map. Each of the following $m$ lines contains $n$ natural numbers from $0$ to $15$, separated by a space, with the meaning: the binary representation of the number on $4$ digits signifies, starting from left to right, the existence of a wall towards the directions $N$, $E$, $S$, $V$. ($1$- wall exists, $0$ – wall does not exist, explanations in the figure below). 
\
~[pereti.jpg|align=left|width=auto] For example, the value $13$ is represented in binary as $1101$, thus correspondingly, from left to right, we will have walls towards $N$, $E$, and $V$.  

# Output data

The output file `pereti.out` will contain on the first line the natural number $k$ representing the length of the walls that will be painted.  

# Constraints and clarifications

* $1 \leq m,n \leq 100$;
* The walls located at the edge of the map are visible walls;
* The input data is considered correct.

# Example

`pereti.in`
```
5 4
0 6 13 1
4 15 5 1
0 14 7 1
4 15 9 0
0 12 5 7
```

`pereti.out`
```
22
```

## Explanation

For positions $(5, 2)$ and $(5, 3)$ the wall between them will be painted on both sides. The wall towards the North of position $(1,3)$ is an external wall, even if it is on the edge of the map.
