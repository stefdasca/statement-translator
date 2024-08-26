## Task

Marcel recently took up a new hobby: creating zen gardens. He quickly developed his own style, which uses $2N$ stones as garden decorations. Half of the stones are green (covered with moss) and are uniquely numbered from $1$ to $N$, while the other half are grey (moss does not grow on them) and are also uniquely numbered from $1$ to $N$. For creating a garden, Marcel will take the stones and place them in a certain order in a straight line, ensuring that the distance between any two consecutive stones is exactly $1$ inch. When it comes to judging the aesthetic appearance of a garden, all gardens are considered beautiful. However, there is a superstition Marcel has about his gardens: if the distance between two stones that have the same number written on them is equal to a multiple of $M$ inches, then the garden is considered $M$-unlucky, bringing great misfortune and causing Code::Blocks errors to the creator. Marcel will never create such a garden. Normally, the rest of the gardens are considered $M$-lucky. As part of his quest for wisdom, Marcel decided to create all possible $M$-lucky gardens. In any case, being also a cautious and organized individual, Marcel would like to know how many $M$-lucky gardens containing $2N$ stones exist before he sets out on his mission. Two gardens $A$ and $B$ are considered different if there exists an integer $i$, $1 \leq i \leq 2N$, such that: the color of the $i$-th stone in garden $A$ is different from the color of the $i$-th stone in garden $B$, or the number written on the $i$-th stone in garden $A$ is different from the number written on the $i$-th stone in garden $B$.

## Input data

The input file `num.in` contains two integers $N$ and $M$, indicating that Marcel will create gardens with $2N$ stones that are $M$-*lucky*.

## Output data

The output file `num.out` contains a single line, print the number of $M$-lucky gardens containing $2N$ stones, modulo $10^9 + 7$.

## Constraints and clarifications

$1 \leq M \leq N \leq 2000$

Scoring

The scoring for each subtask is slightly different from those in the official contest.

Subtask 1 worth 9 points: $N \leq 5$

Subtask 2 worth 12 points: $N \leq 100$

Subtask 3 worth 13 points: $N \leq 300$

Subtask 4 worth 18 points: $N \leq 900$

Subtask 5 worth 48 points: without other restrictions

## Example

`num.in`

100 23

`num.out`

171243255

`num.in`

1 1

`num.out`

0

## Explanation

In the second example, two gardens can be created. However, no garden is $1$-lucky, because for both gardens the distance between the stones numbered with $1$ is $1$ inch, which is a multiple of $M = 1$ inch.