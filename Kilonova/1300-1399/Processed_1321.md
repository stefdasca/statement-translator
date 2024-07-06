Old and wise, the farmer Florea must leave his land as an inheritance to his $P$ sons. Each son has two children, grandchildren of Florea. The farmer's land represents a matrix with $N$ rows and $M$ columns numbered from $1$ to $N$, respectively from $1$ to $M$. Each element of the matrix represents the gain obtained from cultivating agricultural products. The land can be divided into plots. A plot is a succession of neighboring rows in the matrix. Each plot, assigned to a son, must be divided into two lots for the two grandchildren. The first lot consists of the first $K$ columns of the plot, and the second lot of the last $M - K$ columns of each plot. The farmer divides the land into $P$ plots, each being in turn divided into two lots.

The gain of a lot is the sum of the gains from that piece of land. The wise old Florea wants to make a division as balanced as possible among his grandchildren. He wants the sum of differences between the gains of the lots of two grandchildren, children of the same son, to be as small as possible (the difference is considered in absolute value, therefore a positive or zero number).

# Task

Given the configuration of farmer Florea's land and the gain that can be obtained from cultivating agricultural products, calculate the required sum and the number of possible ways to divide the land so as to achieve this value.

# Input data

The first line of the file `parcele.in` contains three natural numbers $N, M, P$ ($N$ respectively $M$ are the coordinates of the farmer's land, $P$ is the number of sons). The following $N$ lines contain $M$ natural values, representing the gains obtained from cultivation.

# Output data

The first line of the file `parcele.out` will contain the value of the required sum. The next line will contain the number of possible ways for Florea to divide his land so as to ensure this minimum value.

# Constraints and clarifications

* $2 \lt N, M \leq 20$
* $2 \leq P \leq N$
* The gain from cultivation is at most $99$.
* The total gain of a lot cannot be zero.

# Example

`parcele.in`
```
4 4 3
3 3 4 3
1 4 3 3
2 4 3 4
1 3 2 4
```

`parcele.out`
```
5
5
```

## Explanation

The minimum difference is $5$. There are five solutions for dividing the land, solutions which are illustrated below.
~[image1.png|align=left]