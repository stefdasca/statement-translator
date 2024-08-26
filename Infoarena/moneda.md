# Coin

You all know the "classic" problem of the $N$ coins (numbered from $1$ to $N$), of which one is different (either heavier or lighter). To identify the different coin (and know whether it is heavier or lighter than the other coins), you have a balance scale with $2$ plates, with which you can perform weighings. A weighing consists of placing the same number of coins on each of the $2$ plates (left and right). The result of a weighing indicates whether the coins on the $2$ plates have the same weight, if the coins on the left plate are heavier, or if the coins on the right plate are heavier. Gigel performed $M$ weighings to identify the different coin. However, after performing the $M$ weighings, he doesn't know how to proceed further, so he asks for your help. Gigel wants to know the minimum additional number of weighings that need to be performed in the worst case to identify the different coin, as well as to know if it is heavier or lighter than the other coins (knowing the weighings performed by Gigel along with their results).

## Task

## Input data

The input file `moneda.in` contains on the first line the numbers $N$ and $T$. Next, $T$ tests will be described, each test corresponding to a case with the same number $N$ of coins. The first line describing a test contains the number $M$ of weighings performed by Gigel. The following $M$ lines describe the weighings. A line describing a weighing has the following format. The first number on the line is the number $K$ of coins that were placed on each of the $2$ plates of the balance. The next $K$ numbers on the line contain the numbers of the coins placed on the left plate, and the next $K$ numbers contain the numbers of the coins placed on the right plate. The last number on the line describes the result of the weighing:  
$0$ - if the weights of the coins on the $2$ plates are equal  
$-1$ - if the coins on the left plate are heavier  
$1$ - if the coins on the right plate are heavier. All numbers on the same line are separated by a space.

## Output data

In the output file `moneda.out` you will print $T$ lines, one for each test given in the input file (in the order the tests are given). On the line corresponding to a test you will print a single number, representing the minimum number of additional weighings needed in the worst case to identify the different coin (and to know if it is heavier or lighter than the other coins).

## Constraints and clarifications

$3 \leq N \leq 60$  
$1 \leq T \leq 10000$  
$0 \leq M \leq 10$  
$1 \leq K \leq N/2$  

It is guaranteed that the answers to the $M$ questions asked by Gigel are not contradictory.

## Example

`moneda.in`  
`8 10`  
`1`  
`1 2 5 0`  
`3`  
`1 2 4 0`  
`2 4 7 5 8 1`  
`1 7`  
`2 1`  
`7 8 -1`  
`4 7 4 3 6 1 8 2 5 -1`  
`2 6 4 2 3 0`  
`1 4 7 0`  
`2 1 7 1 -1`  
`1 7 6 0`  
`1 6 8 -1`  
`4 1 7 1 0`  
`4 5 1 8 3 4 2 7 6 1`  
`2 4 8 3 1 -1`  
`3`  
`2 3 6 5 1 7`  
`1`  
`4 2 1 3 2 5 1 4 8 7 5 6 4 2 3 1`  
`1 8 3 0`  
`4 3 8 1 2 5 4 7 6 -1`  
`3 1 2 7 0`  
`2 8 3 5 4 1`  
`1 6 1 0`  
`3`  
`0 1 0`  
`3 1`  
`0 2 10 20`  
`1 4 10 5 9 3 6 2 8 7 -1`  
`1 3 3 2 7 9 6 8 0`  
`1 3 3 8 10 6 5 4 0`  
`1 3 5 2 4 9 8 3 1 2 5 2 10 9 7 6 1`  
`3 2 4 8 1`  
`4 9 3 10 2 4 6 5 1 0`  
`2 3 2 6 5 3 1 10 0`  
`5 4 8 3 7 1 2 6 5 10 9 -1`  
`1 4 7 1 4 9 2 3 6 10 1`  
`4 3 6 2 3 1 7 5 0`  
`4 7 2 9 10 5 4 1 8 -1`  
`5 9 4 8 2 1 5 10 7 6 3 1`  
`3 6 4 8 5 9 1`  
`2 1 3 5 9 2 10 8 3`  
`1 6 7 5 4 1`  
`4 3 5 7 2 9 10 8 6 -1`  
`5`  
`1 4 10 2 9 6 3 7 8 5 1`  
`1 3 9 3 6 5 10 2 -1`  
`2 4 4 10 7 8 6 9 3 5 -1`  
`3 2 7 4 6 3 9 -1`  
`2 3 2 9 7 3 5 10 0`  
`4 6 1 4 7 5 10 3 9 -1`  
`3 3 2 3 6 8 5 10 1`  
`4 1 8 9 4 3 6 10 5 -1`  
`4 3 2 4 6 7 5 1 8 1 0`  
`3 5 8 6 1 5 10 7 9 3 2 4 -1`  
`4 5 9 10 3 1 8 7 6 0`  
`3 8 4 9 5 10 3 0`  
`1`  
`3 5 6 8 10 9 4 -1`  
`2 5 8 2 6 5 1 3 7 4 9 10 1`  
`3 4 9 6 8 1 10 0`  
`3 5 8 9 4 2 1`  
`5 6 7 3 10 -1`  
`3 7 3 8 6 2 4 0`  
`3`  
`10 6 3 7 4 5 0`  
`4`  
`4 10 3 4 8 2 6 9 5 -1`  
`4 2 6 10 1 7 5 4 9 -1`  
`4 2 4 5 8 7 6 3 9 1`  
`5`  
`1 4 2 6 3 8 5 9 7 10 -1`  
`1`  
`5 1 8 10 6 4 5 2 9 3 7 1`  
`2 2 2 1 2 2`  
`1 2 2 1 1`  
`3 0`  
`2 2 1 0`  
`3`