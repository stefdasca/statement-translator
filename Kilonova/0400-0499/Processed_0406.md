Here's the translated and processed text according to your specifications:

The `N` peasants from the village of Gheorgheni are numbered from `1` to `N` and have their houses arranged chaotically. The houses are represented as `N` points in a plane which have real numbers as coordinates. To better organize their village, they decided to divide the land such that each peasant will receive a plot of land so any point on that plot is closer to his house than to any other house. Points equidistant from `2` or more houses will form the fence, which will not be owned by anyone to avoid conflicts. However, their greed is evident as they forgot about roads ( :)) ). 

Thus, there will be two categories of peasants: dominated (have neighbors all around their yard) and free (have neighbors only in some parts of their yard).

Over time, the village of Gheorgheni has become attractive, and thus `M` more peasants will arrive, each setting their house at a point with real coordinates. After the arrival of each one, the lands are redistributed, and we need to determine the number of free peasants.

# Task
Find and display the number of free peasants initially and after each new peasant arrives.

# Input data
The input file `terenuri.in` contains on the first line `N` and `M`, representing the initial number of peasants of the village of Gheorgheni and the number of peasants who will move into the village. The next `N` lines will contain two real numbers, representing the coordinates of the houses of the initial peasants (natives) (line `i` contains the coordinates of the house of peasant `i`).
Next, there are `M` lines, each containing two real numbers `x` and `y`, representing the coordinates of the house of a new peasant.

# Output data
The output file `terenuri.out` will contain on the first line the initial number of free peasants. 
The next `M` lines contain the number of free peasants after each new peasant arrives.

# Constraints and clarifications

* `3 \leq N \leq 100\ 000`
* `0 \leq M \leq 100\ 000`
* `-1\ 000\ 000\ 000 \leq x, y \leq 1\ 000\ 000\ 000`
* `40\%` of tests will have `M = 0`.
* `20\%` of tests will have `0 < M \leq 100`.
* If a peasant comes to the village, he will never leave
* If you need precision calculations, it is recommended to use `1e-10`

# Example

`terenuri.in`
```
5 1
1.0 1.0
3.0 2.0
2.0 3.0
3.0 4.0
1.0 5.0
6.0 3.0    
```
`terenuri.out`
```
4
3
```
Explanation
---

~[IMAGE.jpg]

In the initial configuration, peasant `3` will be dominated, while the other four peasants will be free.
After the arrival of the new peasant, peasants `2` and `4` will be dominated, while the other `3` will be free.