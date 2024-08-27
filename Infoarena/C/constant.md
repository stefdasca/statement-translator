## Task

Georgel is driving along a road marked kilometer by kilometer. His journey starts from kilometer $0$ and goes up to kilometer $N$. At each kilometer $i$, he notes what traffic sign he sees. Georgel's notes can be represented as a string $S$ of length $N + 1$ such that:

- If $S_i$ is a digit $(1-9)$, it means a zone begins where the maximum speed is restricted to $S_i$
- If $S_i$ is $')'$, it means the end of the previous restriction (which has no pair);
- If $S_i$ is $'*'$, it means there is no sign at kilometer $i$.

Thus, Georgel's notes can be represented as a string like $1*9))$. Each beginning of a zone will have a corresponding end of zone (positions $2-3$ and $0-4$ in the string). Between kilometers $i$ and $i+1$, the restriction imposed by the last sign (with index $\le i$) to which we haven't found the end pair applies (check the example for clarification). Georgel asks himself $Q$ questions of the form "What is the minimum number of matched pairs of signs that need to be removed so that the speed limit between kilometers $a$ and $b$ is constant?" and you need to help him answer them.

## Input data

The input file `constant.in` will contain on the first line an integer $T$, representing the number of tests. The first line of each test will contain two integers $N$ and $Q$ with the meaning from the statement. The second line will contain the string $S$. The next $Q$ lines will each contain two integers separated by a space, $a$ and $b$. There will be an empty line between tests.

## Output data

The output file `constant.out` will contain the answers to the questions. For each test, the answers will be printed on separate lines, in the order of input. There will be an empty line between tests.

## Constraints and clarifications

For all the tests in the evaluation

- $T = 10$
- $1 \leq N \leq 100000$
- $1 \leq Q \leq 100000$
- $0 \leq a < b \leq N$
- $S$ starts with a digit and will end with a character $')'$
- $S$ will not contain the digit $0$
- Removing the pair of signs from positions $0 - N$ in the string is not allowed (because there would be road sections without restrictions)
- The total sums of $N$ and $Q$ will not exceed $500000$

## Example

`constant.in`
```
2
4 4
1*9))
1 3
1 2
0 4
3 4

5 1
55)5))
0 5
1 0 1
0 0
```

`constant.out`
```
1
1
0
0

0
```

## Explanation

The speed limits in the first example are as follows:

Interval | Speed Limit
---------|-----------------
$0 - 1$  | $1$
$1 - 2$  | $1$
$2 - 3$  | $9$
$3 - 4$  | $1$

To make the speed constant between kilometers $1 - 3$, we need to remove the pair of signs restricting the speed to $9$.