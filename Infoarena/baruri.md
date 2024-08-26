# Bars

On Lipscani Street, there are $N$ bars. Since Antonio goes to Lipscani every evening, he wants to know how many friends he has in the surrounding bars to meet with them. Thus, Antonio has created an application that answers questions like: "How many friends are within a maximum distance of $D$ bars from his location?" Since neither he nor his friends can stay in one place, the application needs to know where the friends are moving.

## Input data

The first line of the input file `baruri.in` contains $T$, the number of tests. Further, for each test, the following can be found:
The first line contains the number $N$.
The second line contains $N$ numbers, the $i$th number signifying the number of friends in the $i$th bar.
The third line contains $M$, the number of operations.
The next $M$ lines contain operations: 
0 $B$ $D$ - Display how many friends are in bars within a maximum distance of $D$ bars from the bar $B$ where Antonio is. Those who are already in bar $B$ are considered in his group, so they are not counted.
1 $X$ $B$ - $X$ new friends enter bar $B$.
2 $X$ $B$ - $X$ friends from bar $B$ leave Lipscani.
3 $X$ $B1$ $B2$ - $X$ friends move from bar $B1$ to bar $B2$.

## Output data

The output file `baruri.out` will contain the answers to questions (operations of type 0) in the order they appear.

## Constraints

$1 \leq T \leq 10$  
$1 \leq N \leq 100\ 000$  
$1 \leq M \leq 150\ 000$  
$1 \leq A, B \leq N$  
$X \leq 10\ 000$  
$D \geq 1$  
Although Antonio is very popular, the number of friends can be represented using 32-bit signed integers.

## Example

`baruri.in`
```
1
5
2 1 2 0 0
3
0 2 1
1 3 2
1 4 2
```

`baruri.out`
```
1
0
```

Note: Please ensure to preserve the mathematical values, variable names, and structure while translating.