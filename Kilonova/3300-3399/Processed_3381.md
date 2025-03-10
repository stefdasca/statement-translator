Since today is Halloween night, Vlad and Livia have dressed up as a wizard and a clairvoyant and have gone out for candies. They can start from any point in Sighișoara and end in any other point of the city. Because Sighișoara is situated on a hill, they have decided to move only East or South, meaning downhill; if they were to climb, they would tire too quickly and wouldn't be able to scare anyone.

The city is made up of a grid of $N \times M$ houses; any two adjacent houses in the North-South or East-West direction have a street separating them. Additionally, there are streets along the city's edges. For each house located at coordinates $(i, j)$, the amount of candies $D_{i,j}$ that its resident offers to each child is known.

Vlad and Livia have a secret trick to make any two neighbors give them more candies: whenever they take a street passing between two houses, Livia knocks on the door of one house, Vlad on the other, and the amount of candies received magically becomes the product of the number of candies offered by the residents of the two houses. The downside is that if they walk along the edge of the city and pass by a single house, they won't receive any candy from that street.

# Task

Calculate the maximum number of candies Vlad and Livia can obtain by choosing an optimal route among the houses, moving only in the East and South directions.

# Input data

The first line of the input contains two integers, $N$ and $M$, representing the number of rows and the number of columns of the city. The house at coordinates $(1, 1)$ is the most North-Western in the city.

The next $N$ lines contain $M$ integer values each; the $j$-th value on the $i$-th line represents the number of candies $D_{i,j}$ offered by the house at coordinates $(i, j)$.

# Output data

Print a single integer representing the maximum number of candies Vlad and Livia can obtain by choosing an optimal route on this Halloween night.

# Constraints and clarifications

* $1 \leq N, M \leq 1\ 800$
* $1 \leq X \leq 10\ 000$

|#| Points | Constraints                        |
|-|--------|-----------------------------------|
|1| 17     | $1 \leq N, M \leq 10$            |
|2| 24     | $1 \leq N, M \leq 80$            |
|3| 27     | $1 \leq N, M \leq 300$           |
|4| 32     | No additional constraints.       |

# Example

`stdin`
```
6 6
2 4 5 2 3 2
4 5 2 3 2 1
7 2 9 10 3 5
1 8 10 20 4 6
11 1 2 5 10 1
12 3 4 6 10 2
```

`stdout`
```
618
```

## Explanation

~[img1.png]

$4 \times 7 + 7 \times 2 + 2 \times 8 + 9 \times 10 + 10 \times 20 + 20 \times 5 + 5 \times 10 + 10 \times 10 + 10 \times 2 + 2 \times 0 = 618$