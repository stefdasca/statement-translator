# Margiki

Margiki, affected by the current period, has gained a bit of weight. Knowing that all the gyms are closed, he asks Norocel from the land of $iGorj$ for some ideas. Norocel has a huge palace with $N$ steps (it's hard to have that many floors $+$ attic). He invites Margiki to climb all the $N$ stairs and guarantees he will shed the unwanted pounds. Margiki can climb the stairs in $3$ ways: by stepping with his left foot one step, by stepping with his right foot two steps, or by jumping directly $3$ steps, taking a leap with both feet. Norocel promised Margiki he would reward him with a bottle of water if, when he reaches the $N$th step, he tells him in how many distinct ways he could have climbed all these steps (we are sure that Margiki will manage to reach the steps in any situation). Because the answer is very large, Norocel only wants to know the result modulo $1 000 000 007$ (the remainder when divided by this number).

## Input data

The input file `margiki.in` contains on the first line a single number $N$, representing the number of steps.

## Output data

The output file `margiki.out` will contain on the first line a single number representing the total number of distinct ways to climb the $N$ steps.

## Constraints and clarifications

$1 \leq N \leq 10^{12}$

For $20$ points,

$1 \leq N \leq 15$

For another $20$ points,

$1 \leq N \leq 10^{5}$

For another $20$ points,

$1 \leq N \leq 10^{7}$

Be mindful of the memory limit! The committee wishes you Happy Holidays in advance!

## Example

`margiki.in`

`3`

`margiki.out`

`4`

`96400`

`129153773`

## Explanation

In the first example, Margiki can:

jump one step with his left foot, then $2$ steps with his right foot

OR

jump $2$ steps with his right foot, then one step with his left foot

OR

jump directly all $3$ steps taking a leap with both feet

OR

jump $3$ times one step with his left foot