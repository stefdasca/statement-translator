**Task**

~[Poza1.png|align=right|width=10em]

The new INFO emperor of the ONI2013 land has decided to divide the country into regions coded according to an algorithm established by decree. The country is diamond-shaped, with its center at the coordinate point $(0,0)$ and semi-diagonals $dx$ and $dy$ (as in _figure_ $1$).

The emperor chooses a number $k$, representing the number of stages to be performed, as follows:

* In the first stage, the initial diamond is divided into four equal regions, diamond-shaped, each side being half of the side of the initial diamond;
* In each of the next $k - 1$ stages, any diamond resulting from the previous stage is divided into four equal diamonds, as described in the first stage.

~[Poza2.png|align=right|width=10em]

Thus, after $k$ stages, we will have a total of $4^k$ equal regions, diamond-shaped. 

The coding of the regions is done as follows:

* In the first stage, the initial diamond is divided into four regions, coded counterclockwise with the values $1, 2, 3$, and $4$ (as in _figure_ $2$);
* In each of the next stages, the coding is redone as follows: if the previous diamond had the code $X$ in the previous stage, the four diamonds obtained after the current division will now have the codes $4 \cdot X - 3, 4 \cdot X - 2, 4 \cdot X - 1, 4 \cdot X$ (_figure_ $3$).

# Task

~[Poza3.png|align=right|width=10em]

The emperor wants to know, after the $k$ stages, what is the code of the region where a city given by coordinates ($Cx$, $Cy$) is located.

# Input data

The file `romb.in` will contain the number $T$ of questions (test data sets). Each of the next $T$ lines will contain a set of test data with the values $dx, dy, k, Cx, Cy$, with the aforementioned significance, separated by a space.

# Output data

The file `romb.out` will contain $T$ lines, each line $i$ containing the answer to question $i$, a natural number representing the code of the region where the city with given coordinates is located (for test $i$).

# Constraints and clarifications

* $-20 \ 000 \leq dx, dy, Cx, Cy \leq 20 \ 000$
* $0 < k < 20$
* $0 < T < 10$
* $dx$ and $dy$ are natural numbers, and $Cx$ and $Cy$ are integers
* It is guaranteed that the coordinate point $(Cx, Cy)$ is not at a distance less than $10^{-7}$ from the side of a diamond obtained in the last stage.

# Example

`romb.in`
```
2
10 8 2 6 -2
12 16 3 -2 4
```
`romb.out`
```
15
10
```

# Explanation

The number of tests is $T=2$.

The city with coordinates $(6,-2)$, is located in the region coded with $15$.

The city with coordinates $(-2, 4)$, is located in the region coded with $10$.