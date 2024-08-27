# Truck

At the company where Gigel works, there are $M$ types of trucks, with $N$ trucks of each type. Gigel arranges the company trucks in $N$ rows, placing trucks of the same type only on each column. Thus, a matrix is formed where the rows are numbered from top to bottom from $1$ to $N$, and the columns are numbered from left to right from $1$ to $M$. Each night, a band of thieves comes. The band leader announces: "Tonight, we will steal all the trucks in the rectangular area having the top-left corner at row $x_1$ and column $y_1$, and the opposite corner at row $x_2$ and column $y_2$." The next morning, Gigel sees this and "covers up" the theft: on each row with empty spaces, he shifts to the left all the trucks that are to the right of the empty spot left. For example, for $N = 3$ and $M = 5$, initially, we have the following arrangement:
$1 \ 2 \ 3 \ 4 \ 5$
$1 \ 2 \ 3 \ 4 \ 5$
$1 \ 2 \ 3 \ 4 \ 5$

On the first night, the thieves steal trucks from the rectangle with the top-left corner at row $2$, column $2$ and the bottom-right corner at row $3$, column $3$. Thus, the next day, after Gigel shifts the trucks, the arrangement is as follows:
$1 \ 2 \ 3 \ 4 \ 5$
$1 \ 4 \ 5$
$1 \ 4 \ 5$

If on the second night the thieves again steal from the rectangle with the top-left corner at row $1$, column $1$ and the bottom-right corner at row $3$, column $2$, after the shifts made by Gigel during the day, the arrangement is as follows:
$3 \ 4 \ 5$
$4 \ 5$
$5$

## Task

Knowing how many types of trucks exist at the company initially, how many rows they are arranged in, the number $K$ of days with thefts, and the coordinates of the rectangles from which the thieves steal each night, determine what types of trucks are in a certain column in the final arrangement.

## Input Data

The input file `camion.in` contains on the first line $4$ natural numbers: $N \ M \ K$ and $C$, representing the number of rows on which the trucks have been arranged, the number of columns, the number of nights during which the thieves will steal trucks, and the column number for which we want to find out what types of trucks it contains at the end. Each of the next $K$ lines will contain $4$ natural numbers. On line $i+1$ there are $x_1 \ y_1 \ x_2 \ y_2$, $(x_1 ,y_1)$ representing the row and column of the top-left corner, and $(x_2 ,y_2)$ the row and column of the bottom-right corner of the rectangle from which the thieves steal on night $i$. The numbers on the same line are separated by a space.

## Output Data

The output file `camion.out` will contain $N$ lines, each with an integer. The number on line $i$ will represent the type of truck at row $i$ and column $C$ after $K$ days. If there is no truck on row $i$, the value $0$ will be printed on the respective line.

## Constraints

$1 \leq N \leq 600$  
$1 \leq C \leq M \leq 600$  
$0 \leq K \leq 30000$  
It is not mandatory for the rectangle from which a theft is performed to contain trucks in every spot.

## Example

`camion.in`  
`3 5 3 1`  
`2 2 3 3`  
`1 1 3 2`

`camion.out`  
`3`  
`5`  
`5$