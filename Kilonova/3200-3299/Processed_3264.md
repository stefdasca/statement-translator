# Task

In a village in the hillside area, the $n$ households are situated next to each other along the road, all on the same side. These are numbered starting from the entrance of the village, in order, with numbers from $1$ to $n$. Each household produces only one variety of apples. There may be multiple households that have the same apple variety.

On the occasion of celebrating the village day, it is desired that an exhibition should be organized in one of the houses where apples from all existing varieties in the village are brought.

For a certain variety, it is sufficient to bring apples from just one household among those that produce it.

There is another condition: in the household where the exhibition will be organized, apples must be brought only from households with a smaller order number.

The cost of bringing apples from household $i$ to household $e$ is equal to the distance between the two, i.e., $e-i$.

Determine the minimum cost for organizing the exhibition.

# Input data

The file `mere.in` contains on the first line the number $n$, and on the second line, separated by spaces, $n$ natural numbers representing the apple varieties produced respectively in each of the households $1, 2, \dots, n$.

# Output data

The file `mere.out` contains on the first line a number representing the required value.

# Constraints and clarifications

* $1 \leq n \leq 200 \ 000$;
* The apple varieties are natural numbers of at most $9$ digits;
* For $53$ points, the apple varieties are numbered with consecutive numbers starting with $1$.

# Example

`mere.in`
```
9
1 1 3 3 3 4 4 1 1
```

`mere.out`
```
4
```

## Explanation

If we organize the exhibition in household $8$, the cost of bringing the apples is:
* $0$ for variety $1$;
* $1$ for variety $4$;
* $3$ for variety $3$.