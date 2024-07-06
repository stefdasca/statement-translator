# Squares of Land

Patratețel owns an agricultural land consisting of $n$ plots. He has acquired state-of-the-art seeding machines that operate in a particular manner. Each machine has a seeding capacity $P$ and is fixed on one of the plots. The number of seeds planted by the machine on a plot is determined using the formula $P - d$, where $d$ represents the distance in plots from the seeding machine. In the exact location of the machine, where the distance $d$ is $0$, exactly $P$ seeds are planted. On adjacent plots, the number of seeds decreases as the distance from the machine increases, and the seeding process stops when $P - d$ reaches $0$.

Patratețel's land includes plots with walls, on which seeds cannot be planted. The walls block the spread of seeds beyond the respective plot. The machines also stop the seeding process at the ends of the land, left and right. Two machines can plant seeds on the same plot because they do not interfere with each other.

# Task

Your task is to correct a program already written by someone else that displays how each plot looks after seeding. You can find it [here](teren.cpp) or in the "Attachments" section on the side. In plots with walls, you should display $-1$. For the other plots, indicate the total number of seeds planted, considering the placement of the seeding machines and the presence of walls.

# Input data

The first line contains $L$, the length of the land expressed in the number of plots.
The second line contains $Z$, the number of plots with walls.
The third line contains $Z$ numbers representing the indices of the wall zones. The indices are numbered starting from $1$ (see example).

The next line contains $M$, the number of seeding machines.
In the following $M$ lines, read pairs of values $P$ and $T$, representing:
- $P$ — the seeding power of the machine.
- $T$ — the position of the machine on the land. Indexing starts from $1$.

# Output data

At the end of the seeding process, print the state of each plot of land. For each plot, display the total number of seeds planted in that area. In the case of plots containing walls, display the value $-1$.

The results will be displayed on a single line, separated by space. Each displayed number represents either the number of seeds on a plot or the value $-1$ for plots with walls.

# Constraints and clarifications

- $1 \le L \le 10\ 000$
- $0 \le Z \le L$
- $1 \le M \le 1\ 000$
- For each machine, $1 \le P \le 500$.

# Example 1

`stdin`
```
21
4
1 4 8 21
3
20 2
5 6
3 15
```

`stdout`
```
-1 20 19 -1 4 5 4 -1 0 0 0 0 1 2 3 2 1 0 0 0 -1
```

## Explanation

- Machine $1$ (power: $20$, location: $2$) cannot seed to the left due to the wall, but seeds $19$ seeds to the right, up to the next wall.
- Machine $2$ (power: $5$, location: $6$) seeds to the left and right but is blocked by walls in both directions.
- Machine $3$ (power: $3$, location: $15$) seeds a few seeds in both directions until its power runs out. It does not reach any wall before stopping!

# Example 2

`stdin`
```
5
2
3 5
2
15 2
15 4
```

`stdout`
```
14 15 -1 15 -1
```

## Explanation

- Machine $1$ (power: $15$, location: $2$) can seed on its plot and to the left up to the edge of the land, whereas the wall on plot $3$ blocks it on the right.
- Machine $2$ (power: $15$, location: $4$) seeds only on its plot because it is blocked by walls on both sides.