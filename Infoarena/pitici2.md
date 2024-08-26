# Pitici2

In the dwarves' village, there are $N$ houses, numbered from $1$ to $N$. The village wizard learned from the good fairy that the village is about to be attacked. Using a magical ingredient, he can make the dwarves' houses invisible until the danger passes, thus saving the village. Unfortunately, the wizard does not have enough magical ingredient to hide the entire village, nor does he have time to gather herbs from the forest. Due to the way his spells work, he can only make houses invisible along three lines (not necessarily distinct). Determine if the village can be saved. If so, indicate the lines along which the dwarves' houses are located. In other words, you have to determine the lines that "cover" the dwarves' houses.

## Input data

The first line of the file `pitici2.in` contains a natural number $N$, representing the number of houses. The next $N$ lines contain two integers each, representing the coordinates of the houses.

## Output data

If the dwarves' houses cannot be "covered" by at most three lines, the first line of the file `pitici2.out` will contain the sentence 'Piticii sunt in pericol.' If the village can be saved, the first line of the output file will contain the sentence 'Piticii se vor salva.' The next three lines will contain two natural numbers each, representing the order numbers of the houses, separated by a space, which determine the lines along which the houses in the village are located.

## Constraints

$2 \leq N \leq 5000$ 

The coordinates of the houses will be in the range $[-30\ 000, 30\ 000]$

If there are multiple solutions, only one will be written in the file

Two houses will not be at the same point

## Example

`pitici2.in` 

```
7 
0 0 
0 1 
0 2 
1 1 
2 2 
2 0 
1 0
```

`pitici2.out` 

```
Piticii se vor salva. 
1 2 
1 4 
1 7
```

## Explanation

The line connecting house $1$ with house $2$ also covers house $3$. The line connecting house $1$ with house $4$ also covers house $5$. The line connecting house $1$ with house $7$ also covers house $6$.