A team of researchers has built a robot to perform industrial operations in hard-to-reach environments. The robot is powered by an electric motor fed by a battery with the property of self-charging using ambient energy.

For preliminary tests, a square testing surface was built, consisting of $N \cdot N$ unit-sized squares, with each square having a known amount of energy, possibly zero, that the robot can accumulate if it reaches the respective position. The robot will move according to a string of commands encoded by the characters `N`, `E`, `S`, `V` (`N` - move one position to the north, `E` - move one position to the east, `S` - move one position to the south, `V` - move one position to the west). The string of commands is correct, meaning the robot will not pass through the same position multiple times and will not exceed the edges of the testing surface.

Initially, the robot's battery is completely discharged, but it is assured to be in a position where it can accumulate energy. Moving the robot from one position to another consumes one unit of energy. The amount of energy that can be stored in the battery is unlimited.

The robot stops when it has executed all commands in the given string or when, upon reaching a position, the battery's energy becomes zero and in that position it cannot accumulate energy.

# Task

Given the size of the testing surface, the amount of energy in each position, the initial position, and the sequence of commands, determine the position where the robot stops.

# Input data

The `robot.in` file contains the following structure:

The first line contains the natural numbers $N$, $M$, $L$, $C$ separated by a space, meaning: $N$ - the size of the testing surface, $M$ - the number of commands, $L$ and $C$ - the coordinates of the initial position (row and column, respectively);
The second line contains $M$ characters from the set {`N`, `E`, `S`, `V`}, separated by a space representing the string of commands;
The next $N$ lines contain $N$ natural values, separated by a space, representing the number of energy units available in each position of the testing surface.

# Output data

The `robot.out` file will contain two natural numbers $X$ and $Y$, written on the first line of the file, separated by a space, representing the row number and the column number where the robot stops.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$
* $2 \leq M \leq 5\ 000$
* for $30$% of tests $N \leq 100$
* The amount of energy in a position is a natural number less than or equal to $1\ 000\ 000$
* The rows and columns of the testing surface are considered numbered from top to bottom and from left to right, starting with the value $1$.

# Example

`robot.in`
```
5 4 1 1
S S S E
2 2 3 4 5
0 0 3 0 1
1 4 4 4 4
0 0 5 5 5
0 1 1 0 0
```

`robot.out`
```
4 1
```

