# Order

The tests for this problem are not well-designed enough to correctly distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! There are $n$ children seated in a circle, numbered from $1$ to $n$ counterclockwise. The children play the following game: the game starts with the first child (the one whose order number is $1$); at every $i$-th step of the game, $i$ children are counted counterclockwise, and the child reached is eliminated; at the next step, counting begins from the child who follows the one eliminated. Therefore, if the number of children is sufficiently large, at the first step, the second child is eliminated, at the second step the fourth child, at the third step the seventh, then at the fourth step the eleventh, and so on.

## Task

You will need to determine the order in which the children will be eliminated. 

## Input data

The input file `order.in` contains an integer $n$ on the first line, which represents the number of children. 

## Output data

The output file `order.out` must contain a single line with $n$ distinct numbers between $1$ and $n$ that represent the order numbers of the children in the order they were eliminated. 

## Constraints and clarifications

$2 \leq n \leq 30000$.

## Example

`order.in`

```
6
```

`order.out`

```
2 4 1 3 5 6
```