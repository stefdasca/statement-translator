In the Acrom mountain peak, during summer, $K$ dwarves live, numbered from $1$ to $K$. 

On the mountain, there are $N$ cabins, located at different altitudes, connected by $M$ paths. The dwarves' cabin is numbered $1$, and the cabin at the mountain's base is numbered $N$. 

Since it is too cold in winter, the dwarves move to the cabin at the mountain's base, where it is warmer. The dwarves are disciplined and descend the mountain in increasing order of their numbers. To avoid being accused of lacking personality, each dwarf chooses the shortest path down, a path different from each of the paths chosen by the dwarves who descended before him. A dwarf's path is a sequence of cabins $x_1 \\ x_2 \\ ... \\ x_p$ with the property that $x_1=1, x_p=N$ and between any two consecutive cabins on the path $x_i$ and $x_{i+1}$ there is a path going downhill (meaning the altitude of the cabin $x_i$ is higher than the altitude of the cabin $x_{i+1}$). Two paths are different if there is at least one cabin belonging to one of the paths and not belonging to the other. The length of a path is the sum of the lengths of the paths connecting the cabins on this path.

# Task
Write a program that determines the length of the path chosen by each dwarf, a path that meets the conditions in the statement.
# Input data
The first line of the input file `pitici.in` contains three natural numbers $N \\ M \\ K$ separated by a space with the meaning from the statement. The next $M$ lines contain $3$ numbers $a \\ b \\ c$ separated by a space, meaning there is a path from cabin $a$ to cabin $b$ of length $c$, with cabin $a$ having a higher altitude than cabin $b$.
# Output data
The output file `pitici.out` will contain a single line on which there will be $K$ natural numbers separated by a space. The $i$-th number represents the length of the path chosen by dwarf $i$.

# Constraints and clarifications

* $2 < N < 1\ 020$
* $2 < M < 200\ 020$
* $1 < K < 1\ 020$
* $0 <$ the length of a path $< 1\ 020$
* The correctness of the input data is guaranteed.
* Between any $2$ cabins there is at most one path.
* There will be at least $K$ different paths from cabin $1$ to cabin $N$.
* Cabin $1$ has the highest altitude, while cabin $N$ has the lowest altitude.

# Example

`pitici.in`
```
9 11 3
1 2 1
1 4 1
2 3 1
3 7 4
7 9 1
4 6 2
4 5 1
5 8 4
6 8 1
6 7 2
8 9 2
```

`pitici.out`
```
6 6 7
```

## Explanation

The first dwarf will choose the path consisting of cabins $1 \\ 4 \\ 6 \\ 7 \\ 9$, the path having a length of $6$. The second will choose the path $1 \\ 4 \\ 6 \\ 8 \\ 9$, also of length $6$. The last dwarf will choose the path $1 \\ 2 \\ 3 \\ 7 \\ 9$ with a length of $7$.