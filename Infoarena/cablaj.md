# Cabling

The county's electricity distribution company has decided that the entire network of cables across the county should be completely replaced due to cable wear and tear. The network must be designed in such a way that there is a connection via cable (either direct or indirect, passing through any number of other localities) between any two localities in the county. The cost of cabling between two localities is directly proportional to the distance between the two localities. Each of the localities is located on the map of the county by its Cartesian coordinates, in a coordinate system with the origin somewhere in the southwest of the county, so all coordinates of any locality will be positive. The director of the company, being very busy, asks you to determine the minimum length of cable needed to wire all $N$ localities.

## Input data

The input file `cablaj.in` will contain on the first line $N$, the number of localities, and on the following $N$ lines, the coordinates of the localities.

## Output data

The output file `cablaj.out` will contain a real number representing the total minimum length of the necessary cable.

## Constraints and clarifications

$1 \leq N \leq 3000$

$0 \leq$ coordinates of any locality $\leq 30000$

There will not be multiple localities at the same coordinates.

An error of up to $0.001$ will be accepted.

## Example

`cablaj.in`

```
4
7 4
7 7
11 10
1 15
```

`cablaj.out`

```
18.00
```