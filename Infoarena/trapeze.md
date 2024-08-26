# Trapeze

If you play with $N$ identical round objects and try to form different shapes with all the objects, interesting figures appear. One of the most beautiful figures is the trapezoid. It is formed from multiple lines (at least one). On the first line, there are $A$ objects ($A \geq 1$). On the following line (if it exists), there are $A+1$ objects, and so on until all objects are used. For example, with $15$ objects we can form $4$ distinct trapezoids:

$$* * *$$
$$* * * *$$
$$* * * * *$$
$$* * * * * *$$

$$* *$$
$$* * *$$
$$* * * *$$
$$* * * * *$$

$$*$$
$$* *$$
$$* * *$$
$$* * * *$$

$$* * *$$
$$* * * *$$

It is important that all pieces are used in the construction of any trapezoid and all lines are complete. It is very easy to determine for a given number of objects what is the total number of distinct trapezoids that can be formed. For example, for $15$ objects the total number of trapezoids is $4$. It is harder to determine what is the minimum number of objects required to form exactly $K$ distinct trapezoids.

## Task

For the given value of $K$, determine the minimum number of objects required to form exactly $K$ trapezoids.

## Input data

The input file `trapeze.in` will contain on the first line the natural number $K$.

## Output data

The output file `trapeze.out` will contain a single line that will contain the minimum number of objects necessary to form exactly $K$ trapezoids.

## Constraints

$1 \leq K \leq 100$

## Examples

`trapeze.in`
```
4
```

`trapeze.out`
```
15
```

`trapeze.in`
```
5
```

`trapeze.out`
```
81
```