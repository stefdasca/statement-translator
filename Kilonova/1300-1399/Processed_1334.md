The city hall of Constanța is redeveloping the beach in the Mamaia resort. This beach is represented as a rectangular area with a width of $a$ units and a length of $b$ units. The beach is marked with lines parallel to the sides of the rectangle to form squares with a side length of one unit, called zones. Objects will be placed on the beach: umbrellas and towels. It is assumed that if an object enters a zone, it fully occupies it. There are $u$ umbrellas to be positioned. At most one umbrella can be placed in a zone.

$N$ tourists come and lay their towels on the beach. A towel has a rectangular shape and will be placed parallel to the sides of the rectangle. Tourists can place their towels on free zones or over towels already placed. However, a tourist cannot lay their towel on the beach if the area covered by it includes at least one zone where there is an umbrella.

$M$ locals have favorite areas for placing their towels. A favorite area has the shape of a rectangle with sides parallel to the sides of the rectangle marking the beach. After the tourists finish laying down their towels, the locals check if the zones in the favorite area are free (not covered by towels placed by tourists or umbrellas).

# Task

Write a program that determines:
* the number of tourists who managed to place their towels on the beach;
* the number of locals whose favorite zones are free.

# Input data

The input file `plaja.in` contains on the first line three natural numbers, separated by a space, $a$, $b$, and $u$, having the meanings from the statement. Each of the next $u$ lines contains a pair of natural numbers $x \\ y$, representing a zone where there's an umbrella. The next line in the file contains a natural number $N$, representing the number of tourists. The following $N$ lines describe the tourists' towels. Each line contains $4$ natural numbers $x_1 \\ y_1 \\ x_2 \\ y_2$, representing the corners of a towel. The next line contains a single value, $M$, representing the number of locals. On the next $M$ lines there are $4$ numbers, separated by a space, $x_1 \\ y_1 \\ x_2 \\ y_2$, representing the corners of a favorite area.

# Output data

The output file `plaja.out` contains on the first line two natural numbers separated by a space. The first number represents the number of tourists who have placed their towels on the beach, and the second number represents the number of locals whose favorite zones are free.

# Constraints and clarifications

* The top-left corner of the rectangular area has the coordinates $(1,1)$.
* $3 \\leq a, b \\leq 2000$
* $0 \\leq u \\leq 100$
* $3 \\leq m, n \\leq 100\ 000$
* A towel described by $(x_1, \\ y_1, \\ x_2, \\ y_2)$ will have $1 \\leq x_1 \\leq x_2 \\leq a$ and $1 \\leq y_1 \\leq y_2 \\leq b$.
* A favorite area described by $(x_1, \\ y_1, \\ x_2, \\ y_2)$ will have $1 \\leq x_1 \\leq x_2 \\leq a$ and $1 \\leq y_1 \\leq y_2 \\leq b$.
* For C/C++ work, it is recommended to read using $scanf$ or $fscanf$, as they are faster than $cin$.
* Evaluation: if the first task is answered correctly, you get $40\\%$ of the score. If both tasks are answered correctly, you get $100\\%$ of the score.

# Example

`plaja.in`
```
12 13 1
6 11
4
3 4 7 7
5 6 8 8
9 2 10 3
5 10 8 12
3
1 8 3 13
10 3 12 4
2 10 5 12
```

`plaja.out`
```
3 2
```

## Explanation

The last tourist cannot lay the towel. The favorite area of the 2nd local is not free.