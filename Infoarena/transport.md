## Task

A company that produces water mattresses has $N$ such mattresses in a warehouse, stacked one on top of another (in a pile). Each mattress is characterized by its volume (an integer, expressed in cubic decimeters). To transport them to the store for sale, the company will rent a truck that will have a capacity equal to $C$ cubic decimeters. This truck will need to perform at most $K$ transports (the duration of each transport was estimated and it was concluded that if more than $K$ transports are made, the truck would arrive at the store outside of supply hours, so the mattresses could not be sold). For each transport, the truck can be loaded with mattresses, provided that the sum of the volumes of the mattresses loaded into the truck does not exceed the truck's capacity. Since the mattresses are stacked in a pile, it is not possible to load a mattress into the truck unless all the mattresses above it have been loaded (and possibly transported) first. Since the cost of renting the truck depends on its capacity, the company wants to rent a truck with the minimum capacity that can transport all $N$ mattresses, making at most $K$ transports.

## Input data

The first line of the file `transport.in` contains the integers $N$ and $K$ (separated by a space). Each of the next $N$ lines contains an integer, representing the volume of a mattress. The first of these $N$ lines contains the volume of the mattress at the top of the pile, the second line contains the volume of the second mattress, $\dots$.

## Output data

In the file `transport.out`, print a single integer, representing the minimum capacity that the truck must have in order to transport all $N$ mattresses making at most $K$ transports.

## Constraints and clarifications

$1 \leq N \leq 16\,000$

$1 \leq K \leq 16\,000$

$1 \leq$ the volume of any mattress $ \leq 16\,000$

## Example

`transport.in`
```
6 3
7
3
2
3
1
4
```

`transport.out`
```
8
```

## Explanation

In the first transport, the first mattress is loaded (which has a volume of $7$). In the second transport, the 2nd and 3rd mattresses are loaded (the total volume is $3 + 2 = 5$). In the third transport, the 4th, 5th, and 6th mattresses are loaded (the total volume is $3 + 1 + 4 = 8$).