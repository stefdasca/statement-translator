In a building with $h$ floors, several prisoners are held captive on the ground floor by $T$ terrorists. Each floor of the building has $m \cdot n$ identical rooms. Each room has a numerical code (not necessarily unique) expressed by a number in the range [$0, 255$]. A commando team, composed of $K$ antiterrorism experts, must liberate the prisoners. The commando team is parachuted onto the building and tries to reach the ground floor. The landing location ($x, y$) for each team member on the roof is known. The weight of each team member is expressed in units in the range [$1, 255$]. A member of the team can move "down" through a room of the building only if "his weight passes through that room," according to the following definition.

> Definition: We say that "$a$ passes through $b$" ($a$ >> $b$) if, in the binary representation, the number of $1$ digits of $a$ is less than or equal to the number of $1$ digits of $b$ and the $1$ digits of $a$ are common with some $1$ digits of $b$. Example: "$44$ passes through $174$" ($44$ >> $174$) because $44 = 00101100$ and $174 = 10101110$.

To detect a room that a commando team member can pass through, he can possibly move with a "step" in one of the $8$ directions neighboring his current position (reached by landing or moving "down"). Using the "step," he reaches one of the $8$ neighboring rooms. Prisoners can be freed only if at least $T$ members of the commando team reach the ground floor.

# Task

Determine if the prisoners can be freed or not, as well as the number of commando team members who can reach the ground floor.

# Input data

The text file `kommando.in` has the following structure: the first line contains the values $m$, $n$, $h$, $K$, $T$ separated by a space, with the meanings described above; the next $h$ lines contain the codes of the $m \cdot n$ rooms of one floor, separated by a space; the last $K$ lines of the file contain the weight and the coordinates $x$ and $y$ of the landing position on the roof for each of the $K$ members of the commando team, each on a separate line, separated by a space.

# Output data

The first line of the output file `kommando.out` will contain YES or NO, and the second line will contain the number of commando team members who reached the ground floor.

# Constraints and clarifications

* $2 \leq m,n,h \leq 35$;
* $1 \leq T, K, G_i \leq 255$;
* $0 \leq c_{ijk} \leq 255$;

# Example

`kommando.in`
```
5 5 5 3 2
0 0 0 0 0 0 0 33 0 0 0 0 2 0 0 0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 44 2 0 0 0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 11 0 0 0 0 0 0 2 22 0 0 0 0 0 3 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 66 2 0 0 0 0 0 7 0 15 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 2 2
2 3 3
3 4 4
```

`kommando.out`
```
YES
2
