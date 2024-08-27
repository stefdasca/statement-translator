Pirates

The fierce pirates have arrived in the Miruna Archipelago. They are in search of a sunken treasure and have at their disposal a map to help them. The area where the pirates are located is coded in the form of a matrix with $N$ rows and $M$ columns, having elements from the set $\{0, 1\}$. A land area will be represented by the value $1$, and a water area by the value $0$. We consider that two land areas are part of the same island if it is possible to travel from one area to the other by moving only on land, the movement being made in $8$ directions. The pirates are in the area corresponding to the position $({x1}, {y1})$ on the map, and the treasure is in the area $({x2}, {y2})$. To get to the treasure, the pirates will have to traverse certain islands (possibly none). Since the secret services operate only on land, you must help the pirates reach the treasure by traversing a minimum number of islands. You will need to respond to $Q$ such scenarios.

## Input Data

The input file `pirati.in` contains on the first line $3$ natural numbers $N$, $M$, and $Q$, having the significance described in the statement. The next $N$ lines will contain $M$ characters not separated by a space, representing the map encoding. Each of the following $Q$ lines will contain $4$ natural numbers $x1$, $y1$, $x2$ and $y2$ - the coordinates of the pirates and the sunken treasure respectively.

## Output Data

In the output file `pirati.out` you will print $Q$ natural numbers, one per line, representing the answers for each possible scenario.

## Constraints and Clarifications

$1 \leq N, M \leq 1000$

$1 \leq Q \leq 2500$

$1 \leq x1, x2 \leq N$

$1 \leq y1, y2 \leq M$

Both the pirates and the treasure will be in a water area.

## Example

`pirati.in`
```
3 7 1
1110111
1010101
1110111
2 2 2 6
```

`pirati.out`
```
2
```

## Explanation

The pirates will be forced to cross both islands.