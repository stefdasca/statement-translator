~[Actionare.png|align=right|width=30%]

The company TgM produces balloon inflation panels. A panel of dimensions $n$ x $m$ consists of $n$ rows with $m$ square cells of side $1$. Each cell contains a device that can hold a balloon to be inflated. A balloon has a filling level $ b_i{}_j $ ranging between $1$ (deflated) and the maximum possible filling level $k$. Introducing a new volume of air into a balloon already filled to the maximum level $k$ will cause it to burst (level $k+1$). Each burst balloon is automatically replaced with a new balloon at a filling level of $1$ before introducing a new volume of air into any of the balloons on the panel. Air introduction into certain balloons is done through an operation consisting of the following steps:

- A cylinder-piston system is connected to the device in a cell located at row $x$ and column $y$;
- A non-zero natural value $d$ is selected;
- The Air button on the piston handle is pressed.

Upon pressing the Air button, each balloon located within the square with the top-left corner at ($x$, $y$) with side $d$ advances from the current filling level to the next level. If the square with side $d$ exceeds one or more edges of the panel, air is only transmitted to the balloons inside it. Pressing the button consumes a number of air volume units equal to the number of balloons within the square.

# Task

Given the dimensions of a panel $n$ and $m$, the maximum possible filling level of a balloon $k$, the number $p$ of Air button presses, the initial filling level of each balloon on the panel, and the three values $x$, $y$, and $d$ corresponding to each piston operation, write a program that determines and displays:

1. the number of air volume units consumed after the $p$ Air button presses;
2. the number of burst balloons after the $p$ Air button presses;
3. the maximum filling level of a balloon after the $p$ Air button presses and the number of balloons at this filling level.

# Input data

The input file `balon.in` contains on the first line a natural number $C$, representing the task to be solved ($1$, $2$ or $3$), on the second line four non-zero natural numbers $n$, $m$, $k$ and $p$, with the meaning given above, on each of the next $n$ lines $m$ values representing the initial filling level of the balloons on the respective line, and in the last $p$ lines three natural numbers $x$, $y$, and $d$ corresponding to a piston operation. Numbers on the same line of the file are separated by a space.

# Output data

In the output file `balon.out`:

* if $C = 1$, print on the first line the number of air volume units consumed after the $p$ Air button presses;
* if $C = 2$, print on the first line the number of burst balloons after the $p$ Air button presses;
* if $C = 3$, print on the first line two space-separated numbers representing the maximum filling level of a balloon after the $p$ Air button presses and the number of balloons at this filling level.

# Constraints and clarifications

* $C \in \{1, 2, 3\}$; 
* $1 \leq n, m, d \leq 1\ 000$; 
* $1 \leq x \leq n$ and $1 \leq y \leq m$;
* $3 \leq k, p \leq 1\ 000\ 000$;
* $1 \leq b_i{}_j \leq k$, for any $1 \leq i \leq n$ and $1 \leq j \leq m$;
* For $30$ points, $C = 1$;
* For $35$ points, $C = 2$;
* For $35$ points, $C = 3$.

# Example 1

`balon.in`
```
1
4 6 5 2
1 2 3 3 2 1
1 1 4 3 2 2
3 1 1 1 5 3
2 4 2 4 2 2
2 1 3
3 5 3
```

`balon.out`
```
13
```

## Explanation

$C = 1$, $n = 4$, $m = 6$, $k = 5$ and $p = 2$. 
During the first piston operation, $9$ air volume units are consumed corresponding to the elements marked in yellow in the figure from the task.
During the second piston operation, $4$ air volume units are consumed corresponding to the elements marked in pink in the figure from the task, because only four of the balloons are within the square with side $3$ with the top-left corner at position $(3, 5)$.

# Example 2

`balon.in`
```
2
4 6 5 3
1 2 3 3 2 1
1 1 4 3 2 2
3 1 1 1 5 3
2 4 2 4 2 2
2 1 3
3 5 3
3 2 4
```

`balon.out`
```
2
```

## Explanation

$C = 2$, $n = 4$, $m = 6$, $k = 5$ and $p = 3$.

After the first piston operation corresponding to the triplet $x=2$, $y=1$, $d=3$ the filling levels become:

~[img1.png]

and no balloon has burst.

After the second piston operation corresponding to the triplet $x=3$, $y=5$, $d=3$ the filling levels become:

~[img2.png]

and the balloon at position $x=3$, $y=5$ burst, being automatically replaced with a new balloon.

After the third piston operation corresponding to the triplet $x=3$, $y=2$, $d=4$ the filling levels become:

~[img3.png]

and the balloon at position $x=4$, $y=2$ burst, being automatically replaced with a new balloon. In total, $2$ balloons have burst.

# Example 3

`balon.in`
```
3
4 6 5 3
1 2 3 3 2 1
1 1 4 3 2 2
3 1 1 1 5 3
2 4 2 4 2 2
2 1 3
3 5 3
3 2 4
```

`balon.out`
```
5 2
```

## Explanation

$C = 3$, $n = 4$, $m = 6$, $k = 5$ and $p = 3$. 
After the three piston operations, the filling levels have become:
```
1 2 3 3 2 1
2 2 5 3 2 2
4 3 3 2 2 4 
3 1 4 5 4 3
```

The maximum filling level of a balloon is $5$ and there are two balloons at this filling level.