# Task

Cătălin has a quantum billiard table of dimensions $n \times m$.

Initially, there is a ball in the bottom-left corner of the table, at coordinates $(0,0)$. Every second, the ball will move from the current position $(x,y)$ to $(x+1,y+1)$.

Furthermore, when the ball hits the edge of the table, it will teleport to the opposite side, maintaining its direction:

- If the ball hits the top edge of the table at coordinates $(x,n)$, it will instantly teleport to the bottom edge at coordinates $(x,0)$.
- If the ball hits the right edge of the table at coordinates $(m,y)$, it will instantly teleport to the left edge at coordinates $(0,y)$.

Find the first second when the ball will reach the top-right corner of the billiard table. It is guaranteed that this will always be possible.

# Input Data

The input file `biliard.in` will contain two numbers $n$ and $m$, the dimensions of the billiard table.

# Output Data

The output file `biliard.out` will contain one number, the first second when the ball will reach the top-right corner of the billiard table.

# Constraints and clarifications

- $1 \le n,m \le 10^9$;
- For $5$ points, $n=1$;
- For another $10$ points, $n=2$;
- For another $20$ points, $n,m \le 1\ 000$;
- For another $25$ points, $n,m \le 10^6$;
- For the remaining $40$ points, no additional constraints.

# Example 1

`biliard.in`
```
4 6
```

`biliard.out`
```
12
```

## Explanation

The ball will take the following path:
~[exemplu.png|width=50%]
- $(0,0) \xrightarrow{1s} (1,1) \xrightarrow{1s} (2,2) \xrightarrow{1s} (3,3) \xrightarrow{1s} (4,4) \xrightarrow{0s}$ tp to $(4,0)$
- $(4,0) \xrightarrow{1s} (5,1) \xrightarrow{1s} (6,2) \xrightarrow{0s}$ tp to $(0,2)$
- $(0,2) \xrightarrow{1s} (1,3) \xrightarrow{1s} (2,4) \xrightarrow{0s}$ tp to $(2,0)$
- $(2,0) \xrightarrow{1s} (3,1) \xrightarrow{1s} (4,2) \xrightarrow{1s} (5,3) \xrightarrow{1s} (6,4)$

To reach the top-right corner of the table, the ball took $4+2+2+4=12$ seconds.

# Example 2

`biliard.in`
```
917 980
```

`biliard.out`
```
128380
```

# Example 3

`biliard.in`
```
957423 560507
```

`biliard.out`
```
31567193733
```
