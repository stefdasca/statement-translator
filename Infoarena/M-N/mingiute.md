## Task
Write a program that determines this minimum absolute difference to help Matei Mingiuta decide whether to take the risk or consume the entire quantity of detergent himself. If he cannot distribute the loot safely, print $"-1"$, sealing his fate.

## Input data
The input file `mingiute.in` contains on the first line the numbers $N$ and $M$, followed by the next $N$ lines describing the floors of the dormitory with three integers $st_i, dr_i$ and $nr_i$.

## Output data
The output file `mingiute.out` will contain on a single line the answer to the problem.

## Constraints
$1 \leq N \leq 200$

$1 \leq M \leq 200$

$st_i \leq M - dr_i$ for any $1 \leq i \leq N$

$0 \leq nr_i \leq M$

## Example
`mingiute.in`
```
6 10 
5 3 2 
2 4 2 
3 2 1 
4 4 3 
2 3 1 
4 5 1
```

`mingiute.out`
```
1
```

## Explanation
An optimal distribution could be: 
Floor 1: rooms $5, 9$
Floor 2: rooms $1, 10$
Floor 3: room $3$
Floor 4: rooms $4, 7, 8$
Floor 5: room $2$
Floor 6: room $6$
The maximum difference between the pouches distributed at the beginning of the hallway and those at the end appears for floors $3-6$ and is equal to $1$.