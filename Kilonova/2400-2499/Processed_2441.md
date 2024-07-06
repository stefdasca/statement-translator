You are at a trampoline jumping competition. In the final test, you have to follow a path passing through $P$ control points in a specific order, from which you will collect a stamp at each point.

The path is in the form of a $L \times C$ rectangle made up of trampolines. To increase the difficulty of the path, the organizers have removed trampolines in some places, leaving empty spaces where you cannot land.

Initially, you jump on the spot at the starting point, numbered $0$, and after collecting all the stamps, you need to reach the finish point, numbered $P+1$.

Because mastering control over your movements is an important component of this test, each time you jump you can lengthen or shorten your jump by at most $1$, independently in both directions (north-south and west-east).

You can consider that the length of a jump to the north or west is represented by a positive number, while to the south or east by a negative number. For example, if you moved $1$ to the south on the last jump, on the next jump you can jump on the spot, $1$ to the south, or $2$ to the south.

# Task

What is the minimum number of jumps you need to make to collect all the stamps and reach the finish position? To be sure you have reached the finish position, your last jump must be on the spot.

# Input data

The first line of the input file `trambuline.in` contains two numbers $L$ and $C$, representing the length and width of the path.

The next $L$ lines will consist of $C$ characters, `#` representing a trampoline and `.` an empty space.

The $L+1$ line contains a number $P$, representing the number of control points on the path.

The following $P+2$ lines contain two numbers $X$ and $Y$, representing the starting position, the positions of the $P$ control points, and the finishing position.

# Output data

The first line of the output file `trambuline.out` will contain the minimum number of jumps required to complete the path. If this is not possible, print `impossible`.

# Constraints and clarifications

* $1 \leq L, C \leq 50$;
* $1 \leq P \leq 5$;
* For $0 \leq i \leq P+1$, $1 \leq X_i \leq L$ and $1 \leq Y_i \leq C$.

# Example

`trambuline.in`
```
5 5
#####
#...#
#####
#####
#.#.#
1
1 1
5 5
1 4
```

`trambuline.out`
```
9
```

## Explanation
~[exemplu.png|align=center|width=50%]