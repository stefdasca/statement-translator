```markdown
The inhabitants of the planet Agria, known as agri, decided in the famous year $2012$ to explain to Earthlings how to efficiently harvest a row of $n$ corn plants, numbered in order, with $1$, $2$, $3$, ..., $n$.

The $n$ corn plants are harvested by several agri. The first agri walks along the row, starting from the first corn plant and harvesting the first encountered corn plant, the third, the fifth, and so on until the end of the row.

When he reaches the end of the row, the second agri starts and harvests corn plants following the same rule as the first agri.

The method repeats until all the corn plants are harvested.

Ionel, the Earthling, is trying to discover what this method hides and wonders how many corn plants the first agri harvests, how many agri harvest a row with $n$ corn plants, at which pass the corn plant numbered $x$ is harvested, and what the number of the last harvested corn plant is.

Example: If there are $n = 14$ corn plants in a row, then there are $4$ agri that harvest the corn plants:

~[porumb.png]

* The first agri harvests corn plants $1$, $3$, $5$, $7$, $9$, $11$, $13$;
* The second agri harvests corn plants $2$, $6$, $10$, $14$;
* The third agri harvests corn plants $4$ and $12$;
* The last agri harvests corn plant $8$.

# Task

To help Ionel discover the secret of this method, write a program that reads the two natural numbers $n$ and $x$ and determines:

* the number of corn plants harvested by the first agri;
* the number of agri that harvest the row of $n$ corn plants;
* the pass number during which corn plant $x$ is harvested;
* the number of the last harvested corn plant.

# Input data

The input file `porumb.in` contains on the first line, separated by a space, the two natural numbers $n$ and $x$ with the meaning from the statement.

# Output data

The output file `porumb.out` will contain four lines:

* the first line will contain a natural number representing the number of corn plants harvested by the first agri;
* the second line will contain a natural number representing the number of agri who harvest the $n$ corn plants;
* the third line will contain a natural number, representing the pass number during which corn plant $x$ is harvested;
* the fourth line will contain a natural number, representing the number of the last harvested corn plant.

# Constraints and clarifications

* $1 \leq x \leq n \leq 10^9$;
* The passes are numbered in order, starting with the value 1.
* Correctly solving requirement a) gives 10% of the score.
* Correctly solving requirements a) and b) gives 40% of the score.
* Correctly solving requirements a), b), and c) gives 70% of the score.
* Correctly solving all four requirements gives 100% of the score.

# Example

`porumb.in`
```
14 4
```

`porumb.out`
```
7
4
3 
8
```

## Explanation

$7$ represents the number of corn plants harvested by the first agri.
There are $4$ agri who harvest the row with $n = 14$ corn plants.
The corn plant $x = 4$ is harvested on the 3rd pass, and the last harvested corn plant has the number $8$.
```
