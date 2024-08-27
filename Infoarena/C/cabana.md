# The Cabin

In the forest of hazelnuts, there is a cabin belonging to $N$ dwarfs. The cabin has exactly $K$ rooms where they can sleep. As sleep is very important in the world of dwarfs, they play a game before going to bed: The dwarfs enter the cabin one by one, starting with dwarf 1 up to dwarf $N$, and choose the room where they will sleep. A dwarf chooses a room as follows: They go to the room that has been chosen by the fewest dwarfs. If there are multiple rooms with this property, the dwarf will choose any of them. When Snow White arrives at the cabin, she wonders: In how many ways can the cabin be occupied by the $N$ dwarfs? Two ways of occupying the cabin are considered distinct if at least one room contains different dwarfs. Because Snow White is a kind princess, she asks you for the answer modulo $1000000007$.

## Input data

The input file `cabana.in` contains on the first line a natural number $T$, representing the number of tests. The next $T$ lines contain two numbers $N$ and $K$, with the meaning as described above.

## Output data

The output file `cabana.out` will contain $T$ lines, each line $i$ containing the answer to question $i$.

## Constraints and clarifications

$T = 100000$

$1 \leq N \leq 10^{18}$

$1 \leq K \leq 1000000$

It is guaranteed that all the dwarfs fit in the cabin.

## Example

`cabana.in`
```
2
3 2
5 2
```

`cabana.out`
```
4
8
```

## Explanation

For the first test, there are 3 dwarfs and 2 rooms. The four possibilities are:
1. Room 1 is occupied by dwarfs 1 and 3, and room 2 by dwarf 2.
2. Room 1 is occupied by dwarf 1, and room 2 by dwarfs 2 and 3.
3. Room 1 is occupied by dwarfs 2 and 3, and room 2 by dwarf 1.
4. Room 1 is occupied by dwarf 2, and room 2 by dwarfs 1 and 3.