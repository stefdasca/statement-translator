# Service

The city of Cyclonia is special because both houses and offices are placed in a circle. The total number of inhabitants in the city is $N$, each having their own house and office, so there are a total of $2 * N$ buildings. The distance between any two consecutive buildings is equal to $1$. Knowing that people take the shortest route to work, determine the maximum distance a resident will travel between their house and their office.

## Input data

The input file `serviciu.in` will contain on the first line the number of residents in the city of Cyclonia, $N$. The next $N$ lines will each contain two numbers, with the coordinates of the house and the office of resident $i$ on line $i + 1$ (in this order).

## Output data

The output file `serviciu.out` will print on the first line the maximum distance a resident will travel between their house and their place of work.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

It is guaranteed that there will be no two buildings at the same coordinate.

## Example

`serviciu.in`
```
3
1 4
5 3
2 6
```

`serviciu.out`
```
3
```

## Explanation

The distances from resident $1$'s house to their office are $3$ and respectively $3$, so they can take either of the two roads with a length of $3$. The distances from resident $2$'s house to their office are $2$ and respectively $4$, so they take the road with a length of $2$. The distances from resident $3$'s house to their office are $4$ and respectively $2$, so they take the road with a length of $2$. In the image below, you can see the positions of the buildings in the city of Cyclonia for the configuration in the example (the blue dots are the offices, and the red ones are the homes).

## Image

~[image.png|description=Diagram of Cyclonia city buildings]