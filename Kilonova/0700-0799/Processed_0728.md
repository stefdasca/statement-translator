The chief hunter of King Arthur has been tasked with hunting the first ducks returning from the warm countries. The king, being a man with fixed ideas, asked the hunter to hunt the white ducks with white arrows and the black ducks with black arrows.

The ducks come in rows (flocks) of increasing size: first one, then two, three, five, eight, thirteen, etc. It is observed that the number of ducks in a row is equal to the number of ducks in the two preceding rows. The ducks, being orderly creatures, fly in rows where you will not find two ducks of the same color side by side, each row starting with a white duck.

The hunter knows that if he starts to shoot a duck, he must shoot all the ducks in that row, as survivors will alert the others, and they will never return, and our hunter will lose his job.

# Task

Knowing that the hunter received $ka$ white arrows and $kb$ black arrows, you need to determine how many rows of ducks he has shot down and how many arrows of each type he has left, knowing that he wants to keep his job.

# Input data

The first two lines of the input file `vanatoare.in` contain the numbers ka and kb (in this order).

# Output data

The output file `vanatoare.out` will contain:

* the number of rows shot down on the first line
* the number of white arrows left on the second line
* the number of black arrows left on the third line

# Constraints and clarifications

* $1 \leq ka, kb \leq 2 \cdot 10^9$;

# Example

`vanatoare.in`
```
9
10
```

`vanatoare.out`
```
4
2
6
```

## Explanation

For the example, we have the rows ($A$ - white duck, $N$ - black duck) of ducks:

$A$  
$A \ N$  
$A \ N \ A$  
$A \ N \ A \ N \ A$

