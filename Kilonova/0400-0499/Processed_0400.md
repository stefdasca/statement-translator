In the port of Constanța, two ships filled with cargo are anchored. They repeatedly travel to two different destinations. It is known that the first ship reaches its destination after $X$ weeks, while the second ship takes $Y$ weeks. The return trip takes the same amount of time. The owner of the $2$ ships wants to know after how many days the $2$ ships will depart simultaneously from the port again. It is also known that for handling the cargo, the first ship requires $z1$ days and the second ship requires $z2$ days.

# Task

Write a program that determines the number of days after which the $2$ ships will depart simultaneously from the port they left from.

# Input data
The input file `vapoare.in` contains the two numbers $X$ and $Y$ on the first line, separated by a space, representing the number of weeks needed for the two ships to reach their destinations. The second line of the input file contains the values $z1$ and $z2$, separated by a space, representing the number of days required for the two ships to handle the cargo.

# Output data
The output file `vapoare.out` will contain the number of days after which the two ships will meet again in the departure port.

# Constraints and clarifications
* $0 < X,Y \leq 100000$;
* $0 \leq z1, z2 \leq 31$.

# Example

`vapoare.in`
```
1 2
2 2
```

`vapoare.out`
```
240
```

## Explanation

The first ship needs $16$ days to reach the port from which it departed, and the second ship needs $30$ days, so after $240$ days the two ships meet again in the departure port.