## Transformations

Let $(X, Y)$ be a pair of arbitrary integers. We can apply two types of transformations to such a pair, resulting in the pairs $(X, X+Y)$ or $(X+Y, Y)$. An integer $N$ is given. Determine the minimum number of transformations needed to obtain a pair in the form $(x, N)$ or $(N, x)$, where $x$ can be any integer.

## Input data

The input file `transformari.in` contains the integer $N$.

## Output data

The output file `transformari.out` contains the minimum number of transformations needed to reach the desired pair.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

For 60% of the tests 

$N \leq 2\ 000$

You always start from the pair $(1,1)$.

## Example

`transformari.in`  
5  

`transformari.out`  
3

`transformari.in`  
9  

`transformari.out`  
5

## Explanation

For the first example, one possible solution would be: $(1, 1) \rightarrow (1, 2) \rightarrow (3, 2) \rightarrow (3, 5)$.

For the second example, one possible solution would be: $(1, 1) \rightarrow (2, 1) \rightarrow (2, 3) \rightarrow (2, 5) \rightarrow (2, 7) \rightarrow (2, 9)$.