Certainly! Here is the translated problem statement:

---

Since I did not qualify for ONI, I have a spring break. I took the road map of the country and marked $n$ cities that I consider interesting and worth visiting. I numbered the $n$ cities from $1$ to $n$. The city I live in is numbered $x$.

The vacation is not long, so I decided that I could visit exactly $k$ cities located on a route that simultaneously meets the following conditions (we call such a route *valid*):  
1. The route starts from the city I live in (city $x$).  
2. Between any two consecutive cities on the route, there must be a direct road (a road that does not pass through other cities).  
3. The route passes through exactly $k$ distinct cities.  
4. For any city $y$ on the route, the distance (the number of direct roads traveled) on that route from city $x$ to city $y$ (expressed as the number of direct roads traveled on the route) is minimal (i.e., there is no other route on the map from $x$ to $y$ having a strictly shorter length).  

Two valid routes are considered disjoint if they do not contain the same direct road.

# Task

Since I did not qualify for ONI, write a program to help me determine the maximum number of valid disjoint routes.

# Input data

The input file `trasee.in` contains on the first line four natural numbers $n$, $m$, $x$, and $k$ separated by a space, which represent the number of cities, the number of direct roads between cities, the number of the city I live in and the number of cities on a route, respectively. The next $m$ lines contain the $m$ direct roads on the map, one road per line. Each direct road is specified by two distinct natural numbers between $1$ and $n$, separated by a space, representing the cities connected by that road.

# Output data

The output file `trasee.out` will contain a single line which will contain the maximum number of valid disjoint routes.

# Constraints and clarifications

* $1 \leq n \leq 200$
* $1 \leq x \leq n$
* $1 \leq k \leq n$
* Between any two cities, there can be at most one direct road. Roads are bidirectional.

# Example

`trasee.in`

```
7 8 1 3
1 3
2 3
5 3
4 6
4 7
1 4
6 1
6 7
```

`trasee.out`

```
3
```

## Explanation

The starting city is city $1$. There are four valid routes that pass through exactly $3$ cities, starting from $1$ ($1-3-2, 1-3-5, 1-4-7, 1-6-7$). The maximum number of valid disjoint routes is $3$. One solution could be $1-3-2$, $1-4-7$, $1-6-7$.

~[trasee.png]

---

I have double-checked the statement for potential grammar and/or syntax errors according to the rules of English language.