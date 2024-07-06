Miruna is preparing for a summer vacation. She has already decided to go on a trip to the INFO kingdom with a group of colleagues, where the local currency is called BOSS. She has studied the map of this area and found many interesting things. She knows that the kingdom is on an island with a rectangular land area that can be represented as a matrix with $N$ rows and $M$ columns, where each element is a code for a type of tourist attraction that can be visited. Since arrival and departure from the island are done by plane, she knows the position $(l_0, c_0)$ where she will land and the position $(l_f, c_f)$ where she will depart from the island. She can move to visit tourist attractions only in neighboring cells in the **eight directions** (N, S, E, W, NE, NW, SE, SW), and if the new position has a different code than the one from which she came in the previous step, she has to pay a visitation fee equal to the product of the codes of the two areas (expressed in the local currency, BOSS!!!). Miruna would like to find out the minimum amount necessary to move to the departure place on the island.

# Task

Given the configuration of the kingdom and the starting and ending positions, determine the minimum amount needed to move.

# Input data

The first line of the file `taxa.in` contains the natural values $N$, $M$, $l_0$, $c_0$, $l_f$, $c_f$. The next $N$ lines contain $M$ elements each, the codes of each area, natural numbers separated by a space.

# Output data

The file `taxa.out` will contain a natural number $B$, representing the minimum amount necessary for the trip.

# Constraints and clarifications

* $1 \leq N, M \leq 1000$
* The attractions have codes of natural numbers **less than or equal to $5$**, and the initial and final positions are distinct
* For $30\%$ of the tests, we will have $N, M \leq 100$.
* For $20\%$ of the tests, the matrix contains only $2$ values.

# Example

`taxa.in`
```
5 5 1 1 4 5
1 1 2 2 2
1 2 3 3 3
1 1 3 3 3
2 2 2 2 2
1 1 1 2 1
```
`taxa.out`
```
2
```

## Explanation

The minimum amount needed to move from $(1,1)$ to $(4,5)$ is $2$ BOSSes.