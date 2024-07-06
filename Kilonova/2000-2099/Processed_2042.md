```markdown
# Task

A Monopoly board of side length $n$ is made up of the squares along the edge of a square with side length $n$:

~[monopol.png|align=center|width=50%]
In the square at the top-left corner of the Monopoly board, there is a robot that initially has $b$ units of current in its battery.

Each second, the robot can perform one of the following two actions:

1. The robot will stay in place, and its battery will charge with one unit of current.
2. If the robot's battery has $x \ge 1$ units of current, then the robot will advance $x$ squares on the board, and its battery will discharge by one unit.

If $c=1$, display the number of complete laps the robot will make if it cannot charge its battery.

If $c=2$, display the minimum number of seconds the robot needs to make a complete lap.

The robot completes a lap every time it visits (including passing through) the square at the top-left corner of the board.

# Input data

The first line of the input file `monopol.in` will contain the value $c$.

The second line will contain two numbers $n$ and $b$ - the size of the Monopoly board and the number of units of current initially in the robot's battery, respectively.

# Output data

If $c=1$, then the output file `monopol.out` will contain the number of complete laps the robot will make if it cannot charge its battery.

If $c=2$, then the output file `monopol.out` will contain the minimum number of seconds the robot needs to make a complete lap.

# Constraints and clarifications

- $1 \le c \le 2$;
- $2 \le n \le 10^{12}$;
- $0 \le b \le 10^9$;
- For $15$ points, $c=1$ and $b \le 10^6$;
- For another $15$ points, $c=1$;
- For $15$ points, $c=2$ and $n \le 1 \ 000$;
- For another $20$ points, $c=2$ and $n \le 10 \ 000$;
- For another $20$ points, $c=2$ and $n \le 10^6$;
- For another $15$ points, $c=2$.

# Example 1

`monopol.in`
```
1
2 2
```

`monopol.out`
```
0
```

## Explanation

The robot will not make any complete laps:
~[exemplu1.png|width=20%]

# Example 2

`monopol.in`
```
1
4 5
```

`monopol.out`
```
1
```

## Explanation

The robot will make exactly one complete lap:
~[exemplu2.png|width=20%]

# Example 3

`monopol.in`
```
1
4 8
```

`monopol.out`
```
3
```

## Explanation

The robot will move forward with $8+7+\ldots+1=36$ squares.

Since a board with side length $n=4$ has $12$ squares, the robot will make $\frac{36}{12}=3$ complete laps.

# Example 4

`monopol.in`
```
2
5 6
```

`monopol.out`
```
4
```

## Explanation

~[exemplu5.png|width=30%]

In the first second, the robot will move forward with $6$ squares, and its battery will discharge by one unit.

In the second second, the robot will charge its battery.

In the third second, the robot will move forward with $6$ squares, and its battery will discharge by one unit.

In the fourth second, the robot will move forward with $5$ squares, and its battery will discharge by one unit.

# Example 5

`monopol.in`
```
2
2 2
```

`monopol.out`
```
3
```

## Explanation

In the first second, the robot will charge its battery by one unit.

In the second second, the robot will move forward with $3$ squares, and its battery will discharge by one unit.

In the third second, the robot will move forward with $2$ squares, and its battery will discharge by one unit.

# Example 6

`monopol.in`
```
2
7 0
```

`monopol.out`
```
12
```

# Example 7

`monopol.in`
```
2
1000000 0
```

`monopol.out`
```
4899
```

# Example 8

`monopol.in`
```
2
1000000000000 0
```

`monopol.out`
```
4898979
```
```