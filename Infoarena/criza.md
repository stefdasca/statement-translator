# Crisis

The local government of the town CCEX has constructed a straight road. Each family in the town has established a dwelling along the road, where all family members live and where they keep their supplies. The citizens of the town are very industrious and have accumulated impressive amounts of provisions that exceed their needs. Therefore, the mayor decided that each family will invite a few friends (the same number of friends for each family) on the 6th of June. The number of extra portions accumulated (which can be offered to friends) by each family is known, and each friend will be served exactly one portion. The supplies accumulated by a family can be consumed by the respective family or can be donated to other families, in which case the supplies need to be transported. Families that ensure the transport consume one portion for every meter of the road, regardless of the quantity transported. Write a program that determines the maximum number of friends that can be hosted by each family (the same for all families).

## Task:

### Input data

The input file `criza.in` contains on the first line a natural number $N$ which represents the number of families. The next $N$ lines contain information about the families in the town. More specifically, on line $i+1$ there are two natural numbers separated by space $A_i$ $B_i$, where $A_i$ represents the position where family $i$ lives (expressed in meters from the road entrance), and $B_i$ represents the number of extra portions accumulated by family $i$. The families are specified in the order in which they are placed on the road.

### Output data

The output file `criza.out` will contain a single line that will print the maximum number of friends that can be hosted by each family.

### Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq A_i \leq 10^9$

$0 \leq B_i \leq 10^9$

No two families are situated in the same position.

### Example

`criza.in`

```
4
20 300
40 400
340 700
360 600
```

`criza.out` 

```
415
```