Farmer Ion owns a square-shaped field, divided into $N \times N$ unit squares, where he grows potatoes. To harvest the potatoes, the farmer uses a robot specially designed for this purpose. The robot starts from the top-left square, at coordinates $(1,1)$ and must reach the bottom-right square at coordinates $(N,N)$. The robot's route is programmed by storing a series of commands on a magnetic card. Each command specifies the direction of movement (south or east) and the number of squares to be traversed in that direction. The robot collects the harvest only from the squares where it stops between two commands.

Unfortunately, the card containing the program has deteriorated and the robot's reading unit can no longer distinguish the direction of movement, only the number of steps the robot must take for each command. Farmer Ion must manually input the direction of movement for each command.

# Task

Write a program to determine the maximum amount of potatoes that the robot can collect, assuming Ion manually specifies the direction followed by the robot for each command. The path that yields the maximum harvest must also be determined.

# Input data

The input file `sudest.in` has the following structure:
* The first line contains the natural number $N$, representing the size of the field.
* The next $N$ lines contain $N$ natural numbers, separated by spaces, representing the amount of potatoes in each unit square.
* Line $N+2$ contains a natural number $K$ representing the number of commands on the magnetic card.
* Line $N+3$ contains $K$ natural numbers $C_1,\dots,C_K$, separated by spaces, representing the number of steps the robot must take for each command.

# Output data

The output file `sudest.out` will contain on the first line the maximum amount of potatoes collected by the robot. The next $K+1$ lines will contain, in order, the coordinates of the unit squares that constitute the path yielding the maximum amount of potatoes, one unit square per line. Coordinates on the same line will be separated by a space. The first square in the path will have coordinates `1 1`, and the last will have coordinates `N N`. If there are multiple paths yielding the maximum amount of potatoes collected, one such path will be displayed.

# Constraints and clarifications

* $5 \leq N \leq 100$;
* $2 \leq K \leq 2 \cdot N - 2$;
* $1 \leq C_1, \dots, C_K \leq 10$;
* The amount of potatoes in a unit square is a natural number between $0$ and $100$;
* For each input data set, it is guaranteed that there is at least one path;
* It is considered that the robot collects the harvest from both the starting square $(1,1)$ and the ending square $(N,N)$;
* Correct determination of the maximum collected amount of potatoes is awarded $50\%$ of the test's allocated score; for both the maximum collected amount and the correct path, $100\%$ is awarded.

# Example

`sudest.in`
```
6
1 2 1 0 4 1
1 3 3 5 1 1
2 2 1 2 1 10
4 5 3 9 2 6
1 1 3 2 0 1
10 2 4 6 5 10
5
2 2 1 4 1
```

`sudest.out`
```
29
1 1
3 1
5 1
6 1
6 5
6 6
```

## Explanation

Another possible path is:
```
1 1
1 3
1 5
2 5
6 5
6 6
```

but its cost is $1+1+4+1+5+10=22$.