Lesbulan

The secret services of the USA have information about the area where the terrorist Lesbulan is hiding. He is hiding in a series of $N$ bunkers that cannot be infiltrated. The bunkers are connected by $M$ roads. The only solution to neutralize him would be to bomb the bunkers. To avoid causing an international scandal, only one bunker can be bombed in one night, and after the bombing, the bunker will not be destroyed but immediately rebuilt because Lesbulan is a resourceful man. The secret services have also learned that to avoid revealing his location, he changes the bunker where he will spend the night every evening, and moves to a neighboring bunker from the one the previous night.

## Task

Help the secret services determine if there is a strategy to neutralize Lesbulan!

## Input data

In the input file `lesbulan.in`, the first line will contain an integer $T$ corresponding to the number of bunker configurations in the file. On the following lines, there will be $T$ possible configurations of bunkers. The first line of each test will contain two integers $N$ and $M$. On the next $M$ lines, there will be two integers $X$ and $Y$ separated by a space, representing the existence of a road between bunkers $X$ and $Y$. The tests will be separated by an empty line as shown in the example.

## Output data

The output file `lesbulan.out` will contain $T$ lines, the $i$-th line containing the number 1 if for the $i$-th configuration from the input file there is a strategy to neutralize Lesbulan, or a 0 otherwise.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 50$

## Example

`lesbulan.in`

```
2 
2 1 
1 2 

4 6 
1 2 
1 3 
1 4 
2 3 
2 4 
3 4 
```

`lesbulan.out`

```
1 
0 
```

## Explanation

A strategy for the first case is to bomb city 1 twice.