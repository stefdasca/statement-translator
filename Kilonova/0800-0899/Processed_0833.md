Having multiple cubes at their disposal, Crina and Rareș decided to build buildings by joining two or more towers. The towers were obtained by stacking cubes one on top of another. **The height of a tower** is given by the number of cubes it consists of. The buildings constructed were arranged in a line, side by side, thus forming a street, on which the two children will walk.

~[cladiri.png|width=40em]

For numbering the buildings, Crina and Rareș established the following rules:
* Crina starts from one end of the street and Rareș from the other end; each of them walks through the entire street, passing by each building
* Crina sticks a note on each building, writing the heights of the towers from which it is built, in the order she sees them as she walks past them (for example, for the image above, Crina will stick a note on the first building that reads the number $3112$ because the first tower is made of $3$ cubes, the next two towers of this building are made of one cube each, and the fourth tower is made of $2$ cubes);
* Rareș will do the same, but he starts his walk from the other end of the street. In the example in the image, he will stick a note on the first building he encounters that reads the number $2121$.

At the end of the walk, Crina and Rareș realized there are buildings on which both have stuck notes with identical numbers.

# Task

1. What is the height of the tallest tower and the number of buildings that have such a tower in their construction;
2. What is the number of buildings on which both children stuck notes with identical numbers;
3. What is the smallest number of cubes needed **to complete** the buildings so that on each building, Crina's note contains the same number as Rareș's note. The cubes with which the building was initially built cannot be moved.

# Input data

From the input file `cladiri.in` will be read a natural number $N$ from the first line, representing the number of buildings on the street, followed by $N$ lines, each containing a natural number with all non-zero digits, representing the numbers written by Crina on the notes, in the order she stuck them on the buildings.

# Output data

In the output file `cladiri.out`, the first line will contain two natural numbers separated by a single space that represent, in order, the values requested in task $1$. The second line of the file will contain a natural number, greater than or equal to zero, representing the answer to task $2$, and the third line of the file will contain a natural number greater than or equal to zero, representing the answer to task $3$.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* Each building is composed of at most $9$ towers, and the height of each tower is expressed by a non-zero digit.
* Correctly solving task $1$ accounts for $20$% of the points for each test, correctly solving task $2$ accounts for $40$% of the points for each test, and correctly solving task $3$ accounts for $40$% of the points for each test.
* Respect the output file format! To obtain the points awarded for a task, the answer in the file must be correct and written exactly on the specified line in the statement.

# Example

`cladiri.in`
```
6
3112
2772
42422
1741
27372
1212
```

`cladiri.out`
```
7 3
2
8
```

## Explanation

The tallest tower is made of $7$ cubes. There are $3$ buildings that have towers of this height in their construction, those on which Crina sticks the numbers: $2772, 1741$ and $27372$. Rareș sticks notes with the numbers: $2121, 27372, 1471, 22424, 2772$, and $2113$ on the buildings. Two of these buildings received the same numbers from both Crina and Rareș: $2772$ and $27372$. The value determined according to task $3$ is $8$. One cube is added to the building numbered $3112$, $2$ cubes to the one numbered $42422$, $3$ cubes to the building numbered $1741$, and $2$ cubes to the one numbered $1212$.