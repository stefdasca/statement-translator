Here's the translated text as specified:

---

Dudașu Bank has the shape of a matrix with $N$ rows and $6$ columns. Each element of the matrix represents a room, and each room has $4$ doors that ensure communication with the outside or with neighboring rooms. A gang of $N+6$ thieves wants to break into this bank, but for that, they need a plan that takes into account the bank's security systems. Each thief must enter through an exterior door, pass through one or more rooms, and leave the bank through another exterior door. A thief is not allowed to pass through the same room twice. Two different thieves are not allowed to pass through the same room. Through each room, exactly one thief must pass. For an attack plan, the direction in which a thief traverses their route is not relevant. Once the $N+6$ routes are fixed, it is not relevant which route each of the $N+6$ thieves will take. It is observed that, due to the way a plan is designed, each exterior door must be used, and all $N+6$ thieves must participate in the heist.

# Task
Given $N$, calculate the number of ways in which the plan can be made. Since the calculated number can be very large, the result modulo $44\ 449$ of this number will be displayed.

# Input data
The input file `labirint.in` will contain a single natural number $N$ with the meaning given in the statement.

# Output data
The output file `labirint.out` will contain a single natural number which will represent the remainder modulo $44\ 449$ of the number of ways in which the heist plan can be made.

# Constraints and clarifications
* $ 1 \leq N \leq 100\ 000$;
* Dudașu = locality near the city of Drobeta Turnu-Severin.

# Example

`labirint.in`
```
3
```

`labirint.out`
```
9
```

## Explanation

One of the 9 possible solutions is:
~[img1.jpg|align=center|width=auto]

---