**Mr. G has to climb a staircase with $n$ steps. Normally, with each step he takes, he climbs one step. On $k$ of these steps there is a bottle with a certain number of deciliters of water, let this be $x$. If he drinks all the water from such a bottle, G's strength and mobility increase, so that in the next step he can climb up to $x$ steps, after which, if he does not drink again, he returns to "normal". The water bottles are free. The amount of water contained in these bottles may vary from step to step.**

**On $j$ steps there is a bottle with energy drink. For these bottles as well, the amount of energy drink may vary from step to step. Let's assume that in one of these bottles we have $y$ deciliters of energy drink. If he drinks $q$ ($q \leq y$) deciliters from such a bottle, in the next step G can climb up to $2q$ steps, after which in this case as well, if he does not drink again, he returns to "normal". However, the energy drink costs: for an amount of $q$ deciliters consumed, G must pay $q$ lei.**

**There may be steps on which there is no bottle, but also steps on which there is both a bottle of water and an energy drink. In such situations, there is no point for G to drink both beverages since their effects do not accumulate; he can choose to drink one of the two beverages or not drink anything.**

# Task
Determine $p$, the minimum number of steps G needs to take to climb the staircase, as well as the minimum sum G needs to spend to climb the staircase in $p$ steps.

# Input data
The input text file `scara.in` contains:
- the first line contains a natural number $n$, representing the total number of steps;
- the second line contains a natural number $k$, representing the number of steps on which there are water bottles;
- on each of the next $k$ lines, there are two natural numbers separated by a space, representing the ordinal number of the step on which there is a water bottle and the amount of water in that bottle expressed in deciliters;
- the following line contains a natural number $j$, representing the number of steps on which there are energy drink bottles;
- on each of the next $j$ lines, there are two natural numbers separated by a space, representing the ordinal number of the step on which there is an energy drink bottle and the amount of energy drink in that bottle expressed in deciliters.

# Output data
The output text file `scara.out` will contain a single line on which two natural numbers $p c$ will be written separated by a space, $p$ representing the minimum number of steps, and $c$ the minimum sum spent.

# Constraints and clarifications
* $n \leq 120$
* $0 \leq k \leq n$
* $0 \leq j \leq n$
* The amount of water in any bottle is $1 \leq x \leq 100$
* The amount of energy drink in any bottle is $1 \leq y \leq 100$

# Examples

`scara.in`
```
6
1
1 2
2
4 1
1 2
```

`scara.out`
```
3 2
```

`scara.in`
```
6
1
1 2
2
4 1
1 1
```

`scara.out`
```
4 1
```
