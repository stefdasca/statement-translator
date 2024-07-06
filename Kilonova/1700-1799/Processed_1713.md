The golf course of a rich person, let's call him $P$, has a rectangular shape and consists of $N \cdot M$ square parcels, located at the intersection of $N$ rows and $M$ columns.

P. is paranoid. He cannot stand the idea that someone might enter his course uninvited and step on his grass. Therefore, every night he places all his $K$ guard dogs on one of the parcels of the golf course. But the dogs are also paranoid and none of them tolerates seeing more than at most one other dog if they look along the row or column on which they are placed.

P. has built an observation point on the parcel located at row $N$ and column $M$, and there is the only place where he will not place a guard dog.

# Task

Knowing the dimensions of the golf course, determine the number of possibilities modulo $30\ 011$ in which $P.$ can place his dogs on his golf course.

# Input data

The input file `para.in` contains three natural numbers $N$, $M$ and $K$ on the first line, representing the number of rows, the number of columns of the golf course, and respectively the number of guard dogs.

# Output data

The output file `para.out` contains a single natural number on the first line which represents the number of ways to place the guard dogs on the golf course.

# Constraints and clarifications

* $2 \leq k \leq N$, $M \leq 100$
* No two dogs can be placed on the same parcel

# Example 1

`para.in`
```
2 2 2 
```

`para.out`
```
3
```

## Explanation

There are $3$ possible ways to place the $k = 2$ guard dogs, as shown adjacent:

~[para.png]

# Example 2

`para.in`
```
2 3 3
```

`para.out`
```
3
```

## Explanation

There are $3$ possible ways to place the $k = 3$ guard dogs:

~[para2.png]