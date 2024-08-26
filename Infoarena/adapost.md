# Shelter

A battalion of $N$ soldiers has arrived in a dangerous area and is under heavy bombardment by the enemy. Commander Gigel has a map with the positions of the soldiers and the coordinates of $N$ shelters, each with a capacity of one person, where the soldiers need to reach. He wants to devise a rescue plan for the soldiers that minimizes the risk. The risk of a soldier being injured is directly proportional to the time it takes to reach their shelter, so it is also directly proportional to the distance traveled because all soldiers have constant speed. Gigel wants each soldier to have the best chances, so the maximum distance any soldier needs to travel to their shelter should be minimized. Although the maximum distance should be as small as possible, he also wants the total distance traveled by all soldiers to be minimized to reduce the overall risk.

## Task

Choose a shelter for each soldier so that each shelter has one soldier and both of the above conditions are met.

## Input data

The first line of the file `adapost.in` contains an integer $N$ representing the number of soldiers. The next $N$ lines contain the coordinates of the soldiers, and the next $N$ lines contain the coordinates of the shelters.

## Output data

The file `adapost.out` will contain two real numbers: the maximum value of the soldier-to-shelter distances that meets the requirement and the minimum sum of the distances traveled by the soldiers to their shelters.

## Constraints and clarifications:

1 \leq $N$ \leq 400

For finding the first number, 40% of the test value is awarded, with the remaining points being awarded if both numbers are found.

It is possible for the sum of the soldier-to-shelter distances to be even smaller than the one sought, but in that situation, the maximum distance would be too large.

The points have coordinates in the range $[0,1000]$ and are given with a precision of $0.001$

The maximum difference by which the final result can vary from the correct one is $0.001$

## Example:

`adapost.in`

`
5
6.773 5.394
1.981 1.198
7.062 7.228
2.247 5.785
6.749 2.419
5.382 7.861
5.414 3.397
8.789 3.838
9.436 1.929
5.550 7.901
`

`adapost.out`

`
4.07690 14.76992
`