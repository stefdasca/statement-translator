# Paul wants to learn how to program a robot. Initially, he thought of building a robot consisting of a handle, $10$ buttons arranged in a circular fashion and a screen. The buttons are labeled in increasing order from $0$ to $9$, as shown in the figure.

~[robot.png]

A roboprogram will consist of a sequence of instructions. The instructions can be:

* Dp: The robot's handle moves to the right by $p$ positions ($p$ is a digit)
* Sp: The robot's handle moves to the left by $p$ positions ($p$ is a digit)
* A: The button at the robot's handle's current position is pressed, and the digit written on the button appears on the screen
* T: Program termination (used only once at the end and preceded by at least one $A$ instruction)

Initially, the robot's handle is placed at the button $0$, and the screen is empty. For example, after executing the roboprogram D4AS1AAD6AT, the robot presses the buttons labeled $4$, $3$, $3$, $9$, and the screen will display $4339$.

# Task

Write a program that solves the following tasks:

* reads a roboprogram and determines the number of digits displayed on the screen after executing the roboprogram;
* reads a roboprogram and determines the digits displayed on the screen after executing the roboprogram;
* reads a natural number $N$ and constructs a roboprogram of minimal length such that executing it results in the number $N$ on the screen; since the robot likes to move especially to the right, if there are multiple roboprograms of minimal movement length, the one with the maximum number of $D$ instructions will be displayed.

# Input data

The input file `robot.in` contains on the first line a natural number $C$, representing the task to be solved ($1$, $2$, or $3$). If $C = 1$ or $C = 2$, the second line of the file contains a roboprogram. If $C = 3$, the second line of the input file contains the natural number $N$.

# Output data

The output file `robot.out` will contain a single line.

If $C = 1$, the first line will contain a natural number representing the number of digits displayed on the screen after executing the roboprogram from the input file.
If $C = 2$, the first line will contain the digits displayed on the screen after executing the roboprogram from the input file.
If $C = 3$, the first line will contain the roboprogram requested by task $3$.

# Constraints and clarifications

* $0 \leq N \leq 10^9$;
* The length of the roboprogram read from the input file or written in the output file is at most $1000$ characters.
* If the handle is placed at button $0$ and moves to the right, it will head towards button $1$; if the movement is to the left, it will head towards button $9$.
* For a correct solution to the first task, $10$ points are awarded; for a correct solution to the second task, $30$ points are awarded; and for a correct solution to the third task, $50$ points are awarded. $10$ points are awarded by default.

# Example 1

`robot.in`
```
1
D1AD2AS1AT
```

`robot.out`
```
3
```

## Explanation

$C = 1$, for this test task $1$ is solved.

$3$ digits are displayed on the screen ($132$)

# Example 2

`robot.in`
```
2
S0AD2AS1AT
```

`robot.out`
```
021
```

## Explanation

$C = 2$, for this test task $2$ is solved.

The robot's handle moves $0$ units to the left, thus remaining at button $0$ and pressing it, then moves $2$ units to the right and reaches button $2$, pressing it, then moves $1$ unit to the left and reaches button $1$ and presses this button ⇒ $021$.

# Example 3

`robot.in`
```
3
19332
```

`robot.out`
```
D1AS2AD4AAS1AT
```

## Explanation

$C = 3$, for this test task $3$ is solved. To display the digit $1$, the robot's handle moves $1$ unit to the right and then presses (D1A). To display the digit $9$, from the current position, the robot's handle moves $2$ units to the left and presses (S2A). To display the digit $3$, from the current position, the robot's handle moves $4$ units to the right and then presses (D4A). To display the second digit $3$, the robot's handle remains in the current position and presses the button. To display the digit $2$, from the current position, the robot's handle moves $1$ unit to the left and then presses (S1A). The program ends with the instruction T ⇒ D1AS2AD4AAS1AT