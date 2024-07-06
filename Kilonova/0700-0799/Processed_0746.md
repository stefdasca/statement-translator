Ion has built a villa on the beautiful peak of a mountain. Now, he is designing a special staircase that will go from the road to the villa. The height difference between the road and the villa is $H$ (so this must be the total height of the staircase). The staircase will have $N$ steps, all of the same width, but of heights distinct from one another in pairs.

Ion has noticed that the effort he puts into climbing a step is equal to the height of the step. But if he climbs $x$ steps at once, the effort required is equal to the arithmetic mean of the heights of these $x$ steps he climbs at once plus a constant effort value $p$ (needed to gain momentum).

Being an athletic guy, Ion can climb multiple steps at once, but the sum of the heights of the steps climbed at once must not exceed a maximum value $M$.

# Task

Write a program to determine the minimum effort needed to climb a staircase built according to the problem's constraints, as well as a way to construct the staircase that will be climbed with minimum effort.

# Input data

The input file `scara.in` will contain the first line with $4$ natural numbers separated by a space $H \\ N \\ M \\ p$ (with the meaning given in the statement).

# Output data

The output file `scara.out` will contain
- the first line will contain the minimum effort required (with $2$ decimal places rounded);
- the second line will contain $N$ non-zero natural numbers representing the heights of the $N$ steps of the staircase (in the order from the road to the villa), separated by a space.

# Constraints and clarifications

* $0 < H \leq 75$
* $0 < N \leq 8$
* $0 < M < 14$
* $0 \leq p \leq 10$
* For the test data, the problem always has a solution.
* If there are multiple solutions (ways to construct the staircase to achieve the desired minimum effort), you will display the first solution in lexicographical order.
* We say that the array $x=(x_1, x_2, ..., x_k)$ precedes in lexicographical order the array $y=(y_1, y_2, ..., y_k)$ if there exists $i \geq 1$ such that $x_j=y_j$, for any $j<i$ and $x_i<y_i$.
* If the second decimal place of the minimum effort is $0$, or both decimal places are $0$, it is not necessary to display them. Therefore, in the example the minimum effort could have been written as $9$ or $9.0$.
* $40\%$ of the score is given for the first requirement (the minimum effort).
* If the minimum effort is correct and a correct solution is displayed (that respects the problem constraints and corresponds to the minimum effort), but this solution is not the first in lexicographical order, $80\%$ of the score is obtained. For correctly and completely solving both requirements, $100\%$ of the score is obtained.

# Example

`scara.in`
```
10 4 5 2
```

`scara.out`
```
9.00
1 4 2 3
```

