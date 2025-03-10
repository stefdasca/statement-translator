# Task

In a chess tournament, $n$ animals participated. For each animal, it is known whether it is terrestrial or aquatic, as well as its height $h_i$. The animals are numbered from $1$ to $n$ in the order of the score obtained.

At the awards ceremony, they want to be arranged in **strict** increasing order so that the picture reflects the ranking. Initially, their heights $h_1,h_2,\dots,h_n$ are not necessarily ordered, but since aquatic animals are in an aquarium, the aquarium can be raised above the ground by an integer number of units.

In other words, if $i_1,i_2,\dots,i_k$ are aquatic animals, then $h_{i_1},h_{i_2},\dots,h_{i_k}$ can be increased by the same integer number of units $x$ ($0 \le x \le 10^9$), and in the end, it is desired that $h_1<h_2<\dots<h_n$. Determine if there is a solution, and if there is, display a possible value of $x$.

~[Podium.png|align=center|width=50%]

# Input data

The first line contains a number $n$ (the number of animals). The second line contains $n$ numbers $h_1,h_2,\dots,h_n$ (the heights of the animals). The third line contains $n$ numbers $a_1,a_2,\dots,a_n$ from the set $\{0,1\}$. $a_i=1$ if and only if animal $i$ is aquatic.

# Output data

The first line should contain a single integer $x$, representing the number of units by which the aquarium could be raised so that the condition is met. It must hold that $0 \le x \le 10^9$. If there is no solution, print $-1$.

# Constraints and clarifications

For all tests, it is respected that $2 \le n \le 100\,000$ and $1\le h_i\le 1\,000\,000\,000$.

|#| Points | Constraints                                                    |
|-|--------|---------------------------------------------------------------|
|1|   11   | All animals are of the same type (terrestrial or aquatic).    |
|2|   13   | There is only one aquatic animal.                              |
|3|   24   | $h_i \le 100$                                                 |
|4|   30   | $n \le 1\,000$                                                |
|5|   22   | No additional constraints                                     |

# Example 1

`stdin`
```
4
2 1 6 4
0 1 0 1
```

`stdout`
```
3
```

## Explanation

The example is illustrated in the image above. The heights of the animals after raising the aquarium will be 2 4 6 8. The only other possible solution is $x=4$.

# Example 2

`stdin`
```
5
2 1 4 6 4
0 1 0 0 1
```

`stdout`
```
-1
```

## Explanation

In this case, there is no solution. For example, for $x=3$, we obtain the heights 2 4 4 6 7. These are not in strict increasing order.

# Example 3

`stdin`
```
3
7 7 7
0 1 1
```

`stdout`
```
-1
```

# Example 4

`stdin`
```
4
2 1 2 1
0 0 1 1
```

`stdout`
```
-1
```

# Example 5

`stdin`
```
4
1 2 3 4
1 1 1 1
```

`stdout`
```
1000000000
```

## Explanation

In this case, any solution $0 \le x \le 10^9$ is correct.