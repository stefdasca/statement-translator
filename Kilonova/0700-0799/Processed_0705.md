Gigel has a ribbon consisting of $1\ cm$ wide strips, colored in various colors. The ribbon has $N$ strips, each colored with one of $C$ colors, which we will number from $1$ to $C$. Gigel wants the ribbon to have the same color at both ends, but since he cannot change the colors of the strips, the only possibility remains to cut pieces from the ends.

# Task

Write a program to determine the way of cutting the ribbon such that the strips at both ends have the same color, and the length of the obtained ribbon is maximal.

# Input Data

The input file `panglica.in` contains:

- The first line contains the natural numbers $N$ and $C$ separated by a space;
- The next $N$ lines describe the ribbon: each line contains a natural number from $1$ to $C$, representing in order the colors of the strips that make up the ribbon.

# Output Data

The output file `panglica.out` will contain the next $4$ numbers:

- The first line contains the number of remaining strips;
- The second line contains the number of the color that is found at both ends;
- The third line contains how many strips need to be cut from the beginning of the initial ribbon;
- The fourth line contains how many strips need to be cut from the end of the initial ribbon.

# Constraints and clarifications

* $2 \leq N \leq 10\ 000$;
* $1 \leq C \leq 200$;
* If there are multiple solutions, choose the one which cuts the fewest strips from the beginning of the ribbon.

# Example 1

`panglica.in`
```
6 3
1
2
1
3
2
3
```

`panglica.out`
```
4
2
1
1
```

# Example 2

`panglica.in`
```
5 2
1
2
1
2
2
```

`panglica.out`
```
4
2
1
0
```

