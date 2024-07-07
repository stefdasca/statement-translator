
Recent studies have shown that there is indeed intelligent life on Mars. The problem is that now humanity is at war with the Martians and our best bet for survival is that we need to strike first. On Mars, there is a complex railroad system of $n$ cities connected by $m$ bidirectional railroads.

Earth has called upon the best bomber there is, mister RANDy, to strike down those railroads. Because he is a maniac, he only has one bomb left so he can only strike down a single one of those railroads. RANDy will only target strategic railroads. A railroad is strategic if and only if there exists a pair of cities ($x, y$) such that you can reach $x$ from $y$ and after bombing the given railroad, you can no longer reach $x$ from $y$. 

The Martians are starting to pick up on our plan, so they are now constructing $q$ additional railroads. After the construction of each new railroad, RANDy wants to know how many strategic railroads there are. RANDy now asks you to help him find the answer he seeks.

# Task

Determine the number of strategic railroads after the addition of each new railroad by the Martians.

# Input data

The input will contain on the first line $n$, the number of cities on the Martian surface, $m$, the number of railroads connecting those cities and $q$, the number of additional railroads that the Martians will be constructing.

On the next $m$ lines, you will find a pair ($x, y$), meaning that there is a bidirectional railroad from city $x$ to city $y$.

On the next $q$ lines, you will find a pair ($x, y$), meaning that the Martians will construct a railroad from city $x$ to city $y$.

# Output data

The output will contain $q$ lines. The $i$th line will contain a single number $s$, representing the number of strategic railroads after the Martians have constructed the first $i$ new railroads.

# Constraints and clarifications

* $1 \leq n, m, q \leq 2\ 50000$
* The graph is not guaranteed to be connected
* For tests worth $30$ points, $1 \leq n, m, q \leq 1000$
* For tests worth $40$ more points, $1 \leq n, m, q \leq 100000$
* The scores from the contest might be different than the scores you get here

# Example 1

`stdin`
```
5 4 2
5 1
3 2
2 5
4 2
1 2
5 3
```

`stdout`
```
2
1
```

## Explanation

For the first sample, after the first built railroad, the strategic railroads are ($2, 4$) and ($2, 3$). After the second built railroad, the only strategic railroad is ($2, 4$).

# Example 2

`stdin`
```
6 5 2
5 1
3 2
2 5
4 2
1 2
4 3
6 5
```

`stdout`
```
0
1
```
