# Neighbors

In Drumul Taberei, there is a very peculiar building. In the first year when it was built (let's assume year $1$), it had only one floor, then each year another floor is added, so that in year $X$ the building will have $X$ floors. But that is not the only strange thing. The way each floor is occupied is also very peculiar. On the $1^{st}$ floor, the first floor counting from the bottom, the administrator stays all the time, so it is always occupied. Also, the top floor, being new, is always occupied. The rest of the floors, however, are occupied or free according to the following rules:
- if last year the current floor and the floor below were occupied, then the floor will be free this year
- if last year the current floor and the floor below were free, then the floor will be free this year
- if last year the current floor was occupied and the floor below was free, then the floor will be occupied this year
- if last year the current floor was free and the floor below was occupied, then the floor will be occupied this year 

## Task

Write a program that determines the configuration of the floors after $N$ years from construction.

## Input data

The input file `vecini.in` contains a single natural number $N$, which represents the number of years.

## Output data

The output file `vecini.out` will contain $N$ numbers separated by a space. The numbers represent the state of each floor, starting from the $1^{st}$ floor. The representation is $0$ for free and $1$ for occupied.

## Constraints

$$2 \leq N \leq 100 \, 000$$ 

## Example

`vecini.in`

$5$ 

`vecini.out`

$1 \, 0 \, 0 \, 0 \, 1$