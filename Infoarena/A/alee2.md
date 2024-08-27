# Alley in the Neighborhood

In Andrei's town, people want to socialize as much as possible after the pandemic. Considering they only spent money on food during the pandemic, they thought having unlimited resources would create alleys. An alley is a connection between 2 distinct houses and all houses must have an alley connected to a house in the same neighborhood. Practically, the residents of a neighborhood want to find out in how many ways alleys can be built between 2 different pairs, so that the alleys do not intersect (each house is connected with an alley). Considering that Andrei's town has $Q$ neighborhoods, calculate for each neighborhood with $N$ number of houses how many such alleys can be built by the country's residents? Since this number can be very large, the answer should be modulo $313109$ .

## Task

## Input data

The input file `alee2.in` contains, on the first line, a single natural number $Q$. On the following $Q$ lines there is an even number $N$, representing the number of houses in the neighborhood.

## Output data

The output file `alee2.out` will contain $Q$ lines, each line containing a number - the number of possible ways in which the alleys can be constructed in each neighborhood. This number must be modulo $313109$.

## Constraints and clarifications

$1 \leq Q \leq 10\,000$

$2 \leq N \leq 10^{18}$

For 8 points, $Q \leq 50$, $N \leq 100$
  
For another 8 points, $Q \leq 2000$, $N \leq 10^5$

For another 16 points, $Q \leq 2000$, $N \leq 10^9$

For another 16 points, $Q \leq 2000$, $N \leq 10^{18}$

For another 16 points, $Q \leq 10^5$, $N \leq 10^9$

For another 36 points, $Q \leq 10^5$, $N \leq 10^{18}$

The number of residents in any neighborhood will be even. The houses in each neighborhood are arranged in a circle.

## Example

`alee2.in`

    3

    2

    4

    10

`alee2.out`

    1

    2

    42