You want to go on vacation and have already decided on the destination. Formally, you find yourself at point $(0, 0)$ of a Cartesian coordinate system and need to reach the point with coordinates $(X, X)$. The country you are in has roads parallel to the coordinate axes at each natural number abscissa and ordinate. At any moment, if you are at the point with coordinates $(a, b)$, you have $2$ options for movement: to the point $(a, b+1)$ or to the point $(a+1, b)$. Each such step consumes **one liter** of fuel. You cannot pass through some points of the form $(a, a)$, while at other points with equal abscissa and ordinate, there are gasoline stations where you can "refuel". Through all points where the abscissa does not equal the ordinate, you can pass, but there are no gasoline stations. Your car's fuel tank has a capacity of $K$ liters.

# Task

Determine all distinct routes through which you can reach the destination. Two routes are distinct if they differ by at least one point.

# Input data

The file `calatorie.in` contains on the first line two numbers separated by a space, $X$ and $K$, with the meanings described above. The second line contains a number $N$, which represents the number of points of the form $(a, a)$ that cannot be traversed. On each of the following $N$ lines, there is a number $a$, signifying that the point $(a, a)$ cannot be visited.

# Output data

The file `calatorie.out` contains on the first line a single natural number representing the requested value, modulo $997$.

# Constraints and clarifications

* $1 \leq X \leq 50\ 000$;
* $2 \leq K \leq 50$;
* $0 \leq N \leq 10$;
* The journey starts with a full tank;
* It is guaranteed that there exists at least one route;

# Example

`calatorie.in`
```
3 10
1
1
```

`calatorie.out`
```
8
```