Ernest is a well-known time traveler, skilled in business. This time, he finds himself in California in the year 1851 during the peak of the [Gold Rush](https://en.wikipedia.org/wiki/California_gold_rush). The road network between the cities of California can be represented as a weighted **undirected** multigraph (with costs on edges) with $N$ nodes (cities) and $M$ edges (roads). Ernest wants to transport the gold he discovered on a route from city $1$ to city $2$ using the road network. A route from a city $x$ to a city $y$ represents a sequence of roads that starts at $x$ and ends at $y$. The distance of a route is equal to the sum of the distances of the roads that form it.

He is a good historian and knows about the [San Francisco fire](https://en.wikipedia.org/wiki/San_Francisco_Fire_of_1851) that is about to take place. Unfortunately, he is not a good geographer and does not know which of the cities is San Francisco, hence he does not know which roads could be affected by the fire.

# Task

Ernest is cautious and wants to diversify his routes without sacrificing efficiency. Thus, he wants you to help him find out, for each road between $2$ cities, how many minimum distance routes between cities $1$ and $2$ use this road, modulo $998 \ 244 \ 353$.

# Input data

The first line contains two natural numbers, $N$ and $M$. The next $M$ lines contain the roads between cities in the form $x_i$, $y_i$, $d_i$, representing the fact that cities $x_i$ and $y_i$ are connected by a road of distance $d_i$.

# Output data

To reduce the size of the output file, print a single number, the sum of the answers for all the $M$ edges, calculated modulo $998 \ 244 \ 353$.

# Constraints and clarifications
* $2 \leq N \leq 100 \ 000$;
* $1 \leq M \leq 200 \ 000$;
* $1 \leq x_i, y_i \leq N, \forall i \in \{1, 2, \dots, M\}$;
* $1 \leq d_i \leq 2 \ 000 \ 000 \ 000, \forall i \in \{1, 2, \dots, M\}$;
* Cities are numbered from $1$ to $N$;
* Between two nodes $u$ and $v$ there can be multiple edges;
* For tests worth $33$ points, $1 \leq N \leq 1 \ 000$, $1 \leq M \leq 5 \ 000$;
* For the remaining $67$ points, there are no additional constraints.

# Example

`stdin`
```
4 5
1 3 5
3 4 6
4 2 7
2 1 18
2 3 12
```

`stdout`
```
2
```

## Explanation

There is a single route from city $1$ to city $2$ with a distance of $17$ which uses $2$ roads.
~[poza san francisco.PNG]