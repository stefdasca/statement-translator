# Energies

The tests for this problem are not well designed to correctly differentiate inefficient or incorrect solutions. Click here if you want to help us improve the quality of tests for this problem! Gigel has become the administrator of a thermal power plant. One day, there was a power outage, and thus the power plant is down. Gigel needs to restart it. Knowing the energy produced by each generator and the cost of starting it up, he needs to find a solution with minimal cost to produce an amount of energy equal to or greater than what is necessary to restart the plant.

## Task

Help Gigel find the required solution!

## Input data

The input file `energii.in` has the following format:

$G$ - the number of generators

$W$ - the amount of energy needed to restart the plant

$EG_i$ $CG_i$ - the next $G$ lines contain the amount of energy produced by the generator and the cost required to produce the energy, separated by a space $(1 \leq i \leq G)$

## Output data

The output file `energii.out` has the following format:

$C_{\min}$ - the minimum cost required to restart the plant

or

$-1$ if there is not enough energy to restart

## Constraints and clarifications

$1 < G < 1001$

$1 < W < 5001$

$0 \leq EG_i, CG_i < 10001$

The solution is unique

## Example

`energii.in`

```
3 8
2 4
2 3
8 9
```

`energii.out`

```
9
```