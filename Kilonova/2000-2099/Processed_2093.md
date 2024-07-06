*Due to budget constraints, the miner Gaudeamus could not return to this edition of Moisil++. Therefore, he has prepared the following task:*

# Task

Given the coordinates of $n$ points in the plane, find the number of isosceles trapezoids that can be formed with the given points.

~[trapez.png|width=50%]

$ABDC$ is an isosceles trapezoid if:

1. $AB\\text{ }||\\text{ }CD$
2. $dist(A,C)=dist(B,D)$
3. $A,B,C,D$ are not collinear
4. $dist(A,B) \\neq dist(C,D)$ (otherwise the trapezoid would be a parallelogram).

# Input data

The input file `trapezz.in` contains:

The first line contains the number of points $n$.

Each of the following $n$ lines contains two **integer** numbers $x_i$ and $y_i$ - the coordinates of the given points.

# Output data

The output file `trapezz.out` will contain the number of isosceles trapezoids that can be formed with the given points.

# Constraints and clarifications

- $4 \\le n \\le 1000$;
- $-1000 \\le x_i,y_i, \\le 1000$;
- All points in the input file are distinct;
- **Pay attention to precision errors and file names!**;
- For $10$ points, $n \\le 50$ and $0 \\le y_i \\le 1$;
- For another $10$ points, $n \\le 300$ and $0 \\le y_i \\le 1$;
- For another $10$ points, $0 \\le y_i \\le 1$;
- For another $30$ points, $n \\le 50$;
- For another $20$ points, $n \\le 300$;
- For another $10$ points, any two points $i$ and $j$ have $x_i \\neq x_j$ and $y_i \\neq y_j$;
- For the remaining $10$ points, no further constraints are imposed.

# Example 1

`trapezz.in`
```
9
0 0
1 0
2 0
3 0
4 0
0 1
1 1
2 1
4 1
```

`trapezz.out`
```
3
```

## Explanation

~[exemplu1.png|width=90%|align=center]
The three isosceles trapezoids are $ADHG$, $BDIF$ and $CDIG$.

# Example 2

`trapezz.in`
```
11
-3 -3
-3 -2
-2 0
-1 -2
-1 3
1 4
2 -1
2 2
3 0
4 -2
5 1
```

`trapezz.out`
```
7
```

## Explanation

~[exemplu2.png|width=100%]
The $7$ isosceles trapezoids are: $AKHC$, $BJIC$, $DGHE$, $CEFD$, $DFKJ$, $CDJF$, and $DKFE$.