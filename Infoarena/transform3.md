## Task

After seeing how impressed everyone was when he turned into a pickle, Rick decided to create a device to transform into multiple objects, vegetables, or various species of aliens. However, he has certain restrictions when building the device. Specifically, he knows a number $N$ and $Q$ intervals: $(L_i, R_i)$ which have the property that $L_i \leq L_{i+1}$ and $R_i \leq R_{i+1}$ for any $i < Q$. When programming the device, he has to give it at most $4 * N + 2 * Q$ instructions in the form "$x$ $y$" (without quotes), meaning that if he is currently the object, vegetable, or species numbered $x$, he can transform into the one numbered $y$. The transformation is one-directional, meaning that from state $x$ he cannot "return" directly to $y$ unless there is also the instruction "$y$ $x$". Rick will consider the device well made if there is a way to go from state number $y$ $(N + 1 \leq y \leq N + Q)$ to state number $x$ $(1 \leq x \leq N)$ if and only if $L_{y-N} \leq x \leq R_{y-N}$.

## Input data

The first line of the input file `transform.in` contains the numbers $N$ and $Q$. The next $Q$ lines each contain two numbers, with line $i$ containing $L_i$ and $R_i$.

## Output data

The first line of the output file `transform.out` will contain the number of instructions Rick will program into his device, i.e., $M$ their number. Then, on each of the following $M$ lines, there will be two numbers $x$ and $y$, meaning that from state number $x$ it is possible to transition to state number $y$.

## Constraints

$0 \leq N \leq 1000$

$0 \leq Q \leq 2000$

$1 \leq L_i \leq R_i \leq N$

Rick can use only states between $1$ and $10000$ when programming his device.

If you solve it with at most $2N + 2Q\log N$ edges, you will receive $40\%$ of the points, if you solve it with at most $4N + 2Q$ edges, you will receive $100\%$ of the points.

### Subtasks

Subtask 1 (25 points): All intervals are either prefixes or suffixes.

Subtask 2 (25 points): All intervals have at least one position in common.

Subtask 3 (50 points): No additional constraints.

## Example

`transform3.in`:

```
4 3
1 3
2 3
3 4
```

`transform3.out`:

```
7
5 1
5 8
8 2
8 3
6 8
7 3
7 4
```

## Explanation

In the example Rick shows, he uses state $8$ to reduce the complexity of the device. Indeed, for each of the $Q$ states, it is possible to reach strictly the interval of states specified in the input file. The device being created by him, it is evidently well made.