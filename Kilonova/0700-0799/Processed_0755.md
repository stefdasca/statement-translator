The Great Wizard Prospero has a wonderful garden tended by a multitude of elves whose sole task is to fly along the paths in the early morning hours and sprinkle the plants in the ornamental stone pots located on the edges. There is a fountain at the end of the garden and a main path that starts from the fountain and leads to the entrance. Secondary paths branch off from the main path, forming elongated loops that return to the same place on the main path.

It is known that there are $n$ elves, numbered from $1$ to $n$, each assigned to one of the secondary paths. All of them start from the fountain at $5:00:00$ in the morning with a water pot prepared the night before, traverse the main path to their loop, then follow their loop path, return to the main path, go back to the fountain to refill their water pot, and start over again, doing this until $9:00:00$ when they retreat to the shade for a nap. It is known that all the elves fly without interruption, at the same speed, for the entire duration of exactly $4$ hours. For each elf, the number of seconds needed to reach their loop from the fountain and the number of seconds needed to traverse their loop completely are known. Any elf that arrives at the fountain fills their pot in exactly one second, from a tap located on the edge of the fountain. For example, if the elf in charge of loop $5$ in the figure needs $2$ seconds to reach their loop and $15$ seconds to traverse loop $5$, they will return to the fountain to fill their pot at $5:00:19$ ($2 + 15 + 2$), fill their pot and depart again at $5:00:20$, return again at $5:00:39$ and depart at $5:00:40$, etc.

Two elves cannot fill their pot at the same moment from the same tap.

~[elfi.png]

# Task

Determine the minimum number of taps that the fountain must have so that no elf, at any moment, has to wait to fill their water pot.

# Input data

From the input file `elfi.in`:

* The first line contains $n$, the number of elves;
* The next $n$ lines contain $n$ pairs of values $c_i \\ p_i$ representing the number of seconds from the fountain to their own loop and the number of seconds needed to traverse their loop, respectively.

# Output data

The output file `elfi.out` contains a single line with a single number representing the minimum number of taps required.

# Constraints and clarifications

* $2 \leq n \leq 5\ 000$;
* $1 \leq c_i \leq 100$;
* $1 \leq p_i \leq 100$;

# Example

`elfi.in`
```
5
7 4
7 8
4 5
7 6
2 15
```

`elfi.out`
```
4
```

## Explanation

The first, third, fourth, and fifth elves meet simultaneously at the fountain at $7:12:59$ and fill their pots by $7:13:00$.