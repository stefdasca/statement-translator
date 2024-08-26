# Shelter 2

The Commander sent another battalion of $N$ soldiers into enemy territory and now he needs to protect them. After receiving the map with the soldiers' positions, due to the very poor financial situation he is facing, he concluded that he can only build a single provisional shelter. However, he is also thinking about the general welfare of the soldiers and wants the sum of the distances traveled by the soldiers to the shelter to be as small as possible. Since the Commander is not very good with numbers, the fate of the soldiers is in your hands.

## Task

Find out where the shelter should be placed so that the sum of the distances from the soldiers to it is minimized.

## Input data

The first line of the file `adapost2.in` contains a natural number $N$ representing the number of soldiers and the next $N$ lines contain the coordinates of the soldiers.

## Output data

The file `adapost2.out` should contain two real numbers representing the coordinates where the shelter should be placed.

## Constraints and clarifications:

$1 \leq N \leq 50000$

The points have coordinates in the range $\[0,1000\]$ and are given with 3 decimals.

The maximum difference by which the sum of the distances between the soldiers and the found shelter can vary from the minimum is $0.001$. If it is between $0.001$ and $0.2$ it will still receive $40\%$ of the value of a test.

## Example:

`adapost2.in`

```
3
5.223 
5.591 
2.069 
4.643 
5.628 
0.287
```

`adapost2.out`

```
4.1442 
4.2898 
```