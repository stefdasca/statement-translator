# Apm2

The Glorious People's Republic will benefit from a new road system! The presidential commission tasked with accomplishing this glorious task has completed the work plan, skillfully using the paper and pencils provided by the Republic for every citizen. As everyone knows, the Republic has $N$ large cities, which will be connected by $M$ bidirectional roads, each of these roads having an associated toll necessary for traveling on it. Being dedicated to the common people, the members of the commission have also determined a minimum spanning tree for this new road network, suggesting a series of cheap roads that citizens can use to travel between any two cities in the Republic. However, the Great Leader has other priorities. The Great Son is a big fan of the show Top Gear, and the Great Leader wants the new road network to impress the creators of this show, in case they decide to visit our country. Thus, the Great Leader draws $Q$ new roads on the network plan, roads which, according to his wisdom, cross through impressive landscapes. The Great Leader would like one of these newly drawn roads to be included in the final construction. Eager to fulfill the Enlightened Leader's wish, the commission members are now wondering, for each proposed new road, what is the maximum possible toll they can associate with that road such that it is surely included in the Republic's minimum spanning tree.

## Input data

The input file `apm2.in` will contain on its first line the three numbers $N \ M \ \text{and} \ Q$. Each of the next $M$ lines will describe a road by three integers: $X \ Y \ \text{the \ two \ cities \ connected \ by \ the \ respective \ road \ and} \ T \ \text{the \ toll \ associated \ with \ it}$. Each of the next $Q$ lines will describe a road added by the Great Leader, by two numbers, $A \ \text{and} \ B$ representing the two cities that the respective road connects.

## Output data

The output file `apm2.out` will contain $Q$ lines. Each $i$-th line will contain the answer to the question 'What is the maximum toll we can associate with the $i$-th hypothetical edge such that it is surely included in the minimum spanning tree of the network?'.

## Constraints and clarifications

$2 \leq N \leq 10000$

$1 \leq M \leq 100000$

$1 \leq Q \leq 1000$

The tolls are natural numbers from the interval $[1, 10000]$.

A road is considered to be surely included in the MST if it is present in all possible MSTs.

The $Q$ questions are independent of each other. In other words, the answer for a certain road is calculated assuming it is the only road added to the existing $M$ roads.

It is guaranteed that it is possible to travel between any two cities using the $M$ initial roads of the plan.

## Example

`apm2.in`

```
4 3 2
1 2 7
1 3 2
1 4 1
2 3
3 4
```

`apm2.out`

```
6
1
```

## Explanation

If the road between cities 2 and 3 has a toll of 6, we are sure that it will be included in all possible minimum spanning trees. If we had chosen the toll to be 7, there would be at least one spanning tree that does not contain this road: $(1 \ 2) \ , \ (1 \ 3) \ , \ (1 \ 4)$.