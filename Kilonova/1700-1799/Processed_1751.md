~[robot2.png|align=right]

Students from the Faculty of Computer Science at the University of Cluj have designed robots that dust, plant trees, lay tiles, serve meals, and more. Named "Rosie," the dusting robot has two arms ($\textcolor{red}{S}$ — left and $\textcolor{red}{D}$ — right) equipped with brushes that are rotated using a small motor. The robot's arm is programmed to position itself in front of a surface, and the brushes rotated by the motor sweep the surface, thus dusting it.

For a demonstration, the robot is placed in front of a bookshelf with $N$ shelves numbered in order from bottom to top, from $1$ to $N$. The left arm ($\textcolor{red}{S}$) of the robot is positioned in front of the first shelf, while the other arm ($\textcolor{red}{D}$) is positioned in front of the $K$-th shelf.

~[robot.png|align=right|width=12em]

To dust the shelves, the robot's arms movement is programmed as follows:
* each arm moves **only from bottom to top**, from the shelf it is currently positioned at to the **shelf immediately above it**;
* each minute, **only one of the arms moves**, positions itself in front of the corresponding shelf, and dusts it;
* if **both arms reach the same shelf**, the robot locks and the demonstration ends unsuccessfully.

# Task

Knowing that the demonstration ends when the **right arm ($\textcolor{red}{D}$) of the robot reaches the last shelf of the bookshelf**, write a program that calculates the number $M$ of different ways the robot can be programmed to ensure the success of the demonstration. The program will print the **remainder of the division** of the number $M$ by $64\ 997$.

# Input data

The input file `robot.in` contains on the first line two natural numbers $N$ and $K$, in this order, separated by a space, following the significance from the statement.

# Output data

The output file `robot.out` will contain on the first line a single natural number representing the remainder of the division of the number $M$ by $64\ 997$.

# Constraints and clarifications

* $2 \leq K \leq N \leq 2\ 800$
* the two arms CANNOT move simultaneously;
* an arm can be programmed to move in front of a shelf that has already been dusted;
* a programmed way of the robot is defined by a sequence of movements of the arms $\textcolor{red}{S}$ and $\textcolor{red}{D}$;
* two programmed ways of the robot are different if they contain at least one different movement of $\textcolor{red}{S}$ or $\textcolor{red}{D}$. 

# Example

`robot.in`
```
5 2 
```

`robot.out`
```
5
```

## Explanation

With $\textcolor{red}{X}: Y \rightarrow Z$ we denote the movement of the arm $\textcolor{red}{X}$ from shelf $Y$ to shelf $Z$.
There are $5$ ways to program the robot so that the right arm reaches the last shelf:

1) $\textcolor{red}{D}: 2 \rightarrow 3$, $\ \textcolor{red}{D}: 3 \rightarrow 4$, $\ \textcolor{red}{D}: 4 \rightarrow 5$;
2) $\textcolor{red}{D}: 2 \rightarrow 3$, $\ \textcolor{red}{S}: 1 \rightarrow 2$, $\ \textcolor{red}{D}: 3 \rightarrow 4$, $\ \textcolor{red}{D}: 4 \rightarrow 5$;
3) $\textcolor{red}{D}: 2 \rightarrow 3$, $\ \textcolor{red}{S}: 1 \rightarrow 2$, $\ \textcolor{red}{D}: 3 \rightarrow 4$, $\ \textcolor{red}{S}: 2 \rightarrow 3$, $\ \textcolor{red}{D}: 4 \rightarrow 5$;
4) $\textcolor{red}{D}: 2 \rightarrow 3$, $\ \textcolor{red}{D}: 3 \rightarrow 4$, $\ \textcolor{red}{S}: 1 \rightarrow 2$, $\ \textcolor{red}{D}: 4 \rightarrow 5$;
5) $\textcolor{red}{D}: 2 \rightarrow 3$, $\ \textcolor{red}{D}: 3 \rightarrow 4$, $\ \textcolor{red}{S}: 1 \rightarrow 2$, $\ \textcolor{red}{S}: 2 \rightarrow 3$, $\ \textcolor{red}{D}: 4 \rightarrow 5$.