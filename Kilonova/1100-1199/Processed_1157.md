In a hotel, there are $n$ employees in the Administrative Department. The hotel owner decides to change the staff uniforms in such a way that employees working on different floors wear differently colored clothes, while those working on the same floor wear clothes of the same color. Each employee has a unique code given by a natural number with a maximum of $4$ digits.

# Task

Determine a way to choose the colors of the uniforms that meet the above conditions, as well as the number of possible ways.

# Input data

The input file `hotel.in` has the following structure:

* The first line contains two natural numbers, $n$ and $k$ separated by a space ($k$ is the number of colors).
* The next $n$ lines contain two natural numbers separated by a space, the first being the code and the second the floor associated with the employee.

# Output data

The first line of the output file `hotel.out` will contain the number of possible ways. Knowing that a color is coded by a positive natural number less than or equal to $k$, the file will write on each line (starting with the second) the code of a person and the color of the uniform, values separated by a space. The writing order in the output file will be the same as in the input file.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$
* The number of floors in the hotel $\leq 200$
* $1 \leq k \leq 200$
* If there are multiple solutions, only one will be displayed.
* If no solutions exist, the file will contain a single line with the number $0$.
* The number of ways and the way of choosing the color of the uniforms are scored separately ($70\\%$ of the points for the number of ways and $30\\%$ for the correct choice of the colors of the uniforms).

# Example 1

`hotel.in`
```
4 5
123 2
35 1
430 2
13 0
```

`hotel.out`
```
60
123 1
35 2
430 1
13 3
```

# Example 2

`hotel.in`
```
5 2
12 1
13 0
14 1
10 2
11 0
```

`hotel.out`
```
0
```

