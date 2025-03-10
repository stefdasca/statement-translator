Vasilică is visiting medieval fortresses. Being curious, he tries to discover the secret passages and hideouts. Unfortunately, he got lost and ended up in a room from which he cannot exit except by passing through a labyrinth. There is a map of the labyrinth, a matrix of $n$ rows and $m$ columns, where each element represents a room. Movement in the labyrinth can only be made through adjacent rooms either horizontally or vertically. The labyrinth entrances are marked with `A`, the exits with `C`, and the walled (inaccessible) rooms with `Z`. Exiting the labyrinth can be done from one of the `C` rooms, where in each such room there is a locked helicopter. All helicopters can be opened with the same key, and one key can be found in the `B` rooms. Moving to another room takes $1$ unit of time. To exit the labyrinth, Vasilică enters through one of the entrances marked with `A`, takes the key from a `B` room, and exits the labyrinth through a `C` room. He will enter an `A` room at time $1$. `A` type rooms can be located anywhere on the map. In the path from an `A` type room to a `B` type room, one can pass through a `C` type room without exiting the labyrinth.

# Task

Help Vasilică exit the labyrinth as quickly as possible.

# Input data

The file `labirint.in` contains on the first line the number $n$ of rows and the number $m$ of columns of the map, and on the following $n$ lines, $m$ characters each, representing its elements. The characters can be `_`, `A`, `B`, `C`, `Z` with their meanings as described in the text. `_` represents a room without restrictions (free).

# Output data

The first line of the output file `labirint.out` will contain the number representing the shortest time in which Vasilică can exit the labyrinth.

# Constraints and clarifications

* $1 \leq n , m \leq 1 \ 000$
* there is always a way out
* the operation of taking the key or the helicopter from a room does not consume time 

# Example

`labirint.in`
```
5 6
ZA____
A__Z__
A_C__B
C___Z_
___B_Z
```

`labirint.out`
```
9
```

## Explanation

The shortest time in which Vasilică can exit the labyrinth is $9$ units and we have two options: we start from $A(3,1)$ at time $1$ and reach $B(3,6)$ or $B(5,4)$ at time $6$ (take the key) and exit through $C(3,3)$ at time $9$.