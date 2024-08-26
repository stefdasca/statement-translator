# Cobai

Diorde, the greatest biologist from Tritenii de Jos, is working on creating an elixir that will make his fellow villagers more intelligent. He tests this elixir on $Miki$, the only person in the village who volunteered. To measure his intelligence, $Diorde$ has built a rectangular grid, consisting of $M*N$ rooms. Each room can have at most $4$ doors, oriented towards the $North$, $South$, $East$ and $West$. Some rooms are inaccessible, as they are closed. $Diorde$ has a guinea pig that is smarter than many of the villagers, and he releases it from a room which he will close afterwards, allowing the guinea pig to move freely for a period of time. The guinea pig is equipped with a device that continuously transmits a signal indicating the direction it is moving. This device only detects changes in the direction of the guinea pig. After changing direction, the guinea pig moves at least one position in that direction, and the changes in direction are always $90$ degrees. What does $Miki$ need to do to prove he is more intelligent? Given the grid map (with $.$ marking open rooms and $+$ marking closed rooms) and knowing the position from which the guinea pig started (marked with $*$) as well as the directions it moved, he needs to determine a possible position where the guinea pig might be at the end of that time interval. You need to calculate the probability that $Miki$ guesses a position where the guinea pig might be.

## Task 
Given the grid map (with $.$ marking open rooms and $+$ marking closed rooms) and knowing the position from which the guinea pig started (marked with $*$) as well as the directions it moved, you need to determine a possible position where the guinea pig might be at the end of that time interval. You need to calculate the probability that $Miki$ guesses a position where the guinea pig might be.

## Input data 
The first line of the input file contains the numbers $M$ and $N$, separated by a single space. The next $M$ lines contain $N$ characters each, describing the surface of the planet (the allowed characters belong to the set $\{.,+,*\}$ and have the meanings presented earlier). The next line will describe the information provided by the tracking device, unsplit by spaces. The letter $N$ indicates a move to the north (towards the first row of the matrix), the letter $V$ a move to the west (towards the first column), the letter $S$ a move to the south (towards the last row), and the letter $E$ a move to the east (towards the last column).

## Output data 
The output file will contain a single number indicating the sought percentage. The number will be a real number truncated to $2$ decimal places. 

## Constraints and clarifications
$1 \leq N,M \leq 50$

The number of directional changes is at most $1\ 000$

The guinea pig cannot leave the grid

## Example

`cobai.in`
```
4 5
.....
.+.+.
+....
.++.*
NVS 
```

`cobai.out`
```
28.57
```

## Explanation

The grid contains $14$ rooms that are accessible (those marked with $.$). Moving in the directions $N$, followed by $V$, then $S$, the guinea pig can end up in only $4$ other rooms. This results in a percentage of $28.57$.

~[name.png|]