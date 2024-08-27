# The Land of Never

The map of the $Land\ of\ Never$ has been lost, but fortunately, some details about it are still known. It is known that there are $N$ cities connected by various roads. The roads in the $Land\ of\ Never$ are a bit unusual because if there is a road that goes from city $i$ to city $j$, there is not necessarily a road that goes from city $j$ to city $i$. Also, there won't be roads that start and end in the same city, and there won't be multiple identical roads (i.e., roads that have the same start and end cities). For each city, it is known how many roads lead out of it and how many roads lead into it.

## Task

Write a program that determines the roads on the initial map.

## Input Data

The first line of the input file `$harta.in$` will contain the integer $N$, representing the number of cities. Then, $N$ lines follow, where line $i$ contains two numbers $x,y$, the number of roads that lead out of city $i$ and the number of roads that lead into city $i$, respectively.

## Output Data

In the file `$harta.out$`, print on the first line the number $M$ of constructed roads, followed by $M$ lines, each containing a pair of numbers $a,b$ which signify that there is a road that goes from $a$ to $b$.

## Constraints and Clarifications

$1 \leq N \leq 100$

## Example

$harta.in$ 
```
4
2 1
0 2
2 1
1 1
```

$harta.out$
```
5
1 2
1 3
3 2
3 4
4 1
```