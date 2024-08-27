## Task

The Galactic Federation Parliament, worried about the declining population, has decided to throw a bone to every citizen in the galaxy. More precisely, the Parliament has decided to pay a bonus to every citizen whose age is a round number (years have the same duration on all planets due to the Standard Galactic Calendar). Skeptics objected that species use different bases in their numbering systems, so round numbers cannot be defined. After much deliberation, the Parliament decided that an age $A$ will be considered round if it can be written as (two digits of 1 and zero or more digits of 0) in a base $B$, whatever that may be. The amount of the bonus is the smallest base $B$, in which the number $A$ is round. Once the law came into effect, the Parliament needed a quick method to determine the bonuses so that citizens could receive the money before the next elections.

## Input data

The input file `bonus.in` contains on the first line the number $N$, representing the number of citizens in the galaxy. The next $N$ lines contain integers $A_1$, $A_2$, $A_3$, $\dots$, $A_{N}$, representing the ages of the citizens.

## Output data

The output file `bonus.out` contains $N$ lines. Line $i$ must contain a single number, the smallest base in which $A_i$ is a round number.

## Constraints

$1 \leq N \leq 100000$ for 20% of the tests

$1 \leq N \leq 10000$

$2 \leq A_i \leq 2^{64} - 1$ for any $1 \leq i \leq N$

## Example

`bonus.in`

`5`

`36`

`26`

`80`

`56`

`125`

`bonus.out`

`2`

`5`

`2`

`7`

`124`

## Explanations

$36_{10} = 100100_2$

$26_{10} = 101_5$

$80_{10} = 1010000_2$

$56_{10} = 110_7$

$125_{10} = 11_{124}$

## Explanation

Some numbers are round in multiple bases. For example, $36$ is also round in base $3$: $36_{10} = 1100_3$. However, the answer must always be the smallest base.