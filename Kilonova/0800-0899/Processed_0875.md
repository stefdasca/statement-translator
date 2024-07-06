In *The Quiet City* a number of $k$ young friends wish to participate in a protest rally. Since the neighborhood where they live is large, they will travel to the meeting point in their personal cars. Each young person will bring with them a placard on which they have drawn a single letter from the set $\\{$`A`$,`B`$,\\ \\dots,`Z`$\\}$. No two placards have identical letters. The $k$ letters form a word, let's denote it $cuv$, which is known.

The neighborhood where the young people live can be encoded by a matrix with $n \\cdot m$ square zones, some of which are forbidden. It is known that a car consumes one unit of fuel when moving from one zone to an adjacent zone and does not consume fuel if it remains stationary. Two zones are adjacent if they share a side. To save fuel, the young people decide that if two cars meet in one zone and all the letters in the two cars form a subsequence of the word $cuv$, then they will continue the journey together in one car, taking all the placards with them. Otherwise, the cars will continue their journey separately.

For example, if the word $cuv$ is `JOS`, then the car carrying the letter `J` can take the young person bringing the placard with the letter `O`, or vice versa: the car with the letter `O` can take the young person bringing the letter `J`. Then they can continue their journey towards the car carrying the letter `S`. In another scenario, the letters `S` and `O` can first be gathered into one car if the cars carrying them meet in the same zone. However, a transfer, i.e., a gathering of the letters, cannot be made between the car carrying only the letter `J` and the one carrying only the letter `S`.

# Task

Given the dimensions of the neighborhood $n$ and $m$, the word $cuv$, the configuration of the neighborhood, and the initial positions of the young people, determine:

1. The minimum area of a submatrix of the matrix encoding the neighborhood, containing all the initial positions of the young people.
2. The minimum number of fuel units consumed by all the cars, knowing that in the end all the young people will be gathered into one car.

# Input data

The input file `miting.in` contains:

The first line contains a natural number $p$, which can only have the value $1$ or $2$.

The second line contains two natural numbers $n$ and $m$, separated by a space.

The third line contains the word $cuv$.

The next $n$ lines contain $m$ characters per line representing the zones of the neighborhood. A zone is forbidden if it corresponds to the character `#`, it is free if it corresponds to the character `_` (underline), and it is the starting point of a car if it corresponds to one of the letters in the word $cuv$.

# Output data

If the value of $p$ is $1$, **only task $1$** will be solved.  
In this case, the output file `miting.out` will contain a single natural number $A$, representing the minimum area of a submatrix of the matrix encoding the neighborhood, containing all the initial positions of the young people.

If the value of $p$ is $2$, **only task $2$** will be solved.  
In this case, the output file `miting.out` will contain a single natural number $C$, representing the minimum number of fuel units consumed by all the cars until the young people, and thus the letters, are gathered into one car. If there is no solution, meaning not all the young people can be gathered into one car, $-1$ will be printed.

# Constraints and clarifications

* $2 \\leq n, m \\leq 60$
* $2 \\leq k \\leq 10$
* Let $z$ be the number of forbidden zones. Then $0 \\leq z \\leq \\frac{n \\cdot m}{3}$.
* In each time unit, a car can either stay in place waiting for another or move to an adjacent zone, regardless of whether that zone is already occupied by another car.
* The side length of a zone is considered equal to $1$.
* Correctly solving the first task scores $20$ points, while the second task scores $80$ points.
* For $30\\%$ of the test cases of task $2$, it is guaranteed $k \\leq 3$.

# Example 1

`miting.in`
```
1
4 5
JOS
#_O_#
_#__S
_#J_#
___#_
```

`miting.out`
```
9
```

## Explanation

The submatrix with the minimum area that includes all the letters has the top-left corner at row $1$ and column $3$ and the bottom-right corner at row $3$ and column $5$. The area is equal to the number of covered zones: $3 \\cdot 3 = 9$.

**Attention! For this test only task $1$ is solved.**

# Example 2

`miting.in`
```
2
5 7
BUN
_#_#_#_
__N#__#
_#__B__
U__#_#_
_#_#_#_
```

`miting.out`
```
6
```

## Explanation

~[miting_1.png]

One variant of minimum fuel consumption is: `U` moves two positions to the right. Then `B` moves two positions to the left. `U` moves up one position again. Finally, `N` moves down one position. 

Notice that `B` reunited with `U`, then `BU` with `N`.

**Attention! For this test only task $2$ is solved.**

# Example 3

`miting.in`
```
2
6 7
ROST
O#_#_#_
___#__#
_#_R___
____#__ 
__#_S_#
_#_T_#_
```

`miting.out`
```
9
```

## Explanation

~[miting_2.png]

One variant of minimum fuel consumption is: `O` moves down one position, then two positions to the right, moves down one position, and finally one position to the right, where it reunites with `R`. Then `S` moves left one position. `T` moves up one position and reunites with `S`. Finally, the car in which `S` and `T` are located moves up two positions and meets the car in which `R` and `O` are located. In this zone, at row $3$ and column $4$, all the letters are reunited in one car.

**Attention! For this test only task $2$ is solved.**