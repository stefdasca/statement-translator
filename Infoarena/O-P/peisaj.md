Landscape

Gigel's sister has a large box of sticks with which she tries to "draw" horizon lines. Corresponding to the sea level, she chose a straight edge of the carpet, from where she starts placing the sticks in such a way that they form mountains and valleys as in the figure below.

## Task

Help Gigel answer the following questions posed by his sister:
1. How many different horizon lines can be "drawn" with the existing $N$ sticks?
2. How many lines of length $N$ will have a mountain of height at least $K$?
3. How many horizon lines will contain exactly $K$ mountain peaks? (A mountain peak is defined as two sticks placed in a line in the shape of /\).

## Input data

The input file `peisaj.in` contains on the first line two natural numbers $N$, representing the number of sticks, and $K$.

## Output data

In the output file `peisaj.out`, three natural numbers will be written on the first line, answering the three questions above.

## Constraints

$1 \leq N \leq 50$  
$1 \leq K \leq 10$  

The stick with which the line starts and the one with which it ends must necessarily touch the edge of the carpet from the side where the horizon lines were built. No stick can go beyond the edge of the carpet. All angles $\backslash$ / and $\backslash$ \ \ must be $60^\circ$.

Partial scores are awarded as follows:
- subpoint 1. 20%
- subpoint 2. 40%
- subpoint 3. 40%

## Example

`peisaj.in`
```
6 2
```

`peisaj.out`
```
5 4 3
```

## Explanation

The figures that can be formed with 6 sticks are:
- There are 5 horizon lines,
- 4 of them have a mountain of height at least 2,
- and 3 contain exactly 2 mountain peaks.