## Task

The game Chomp is played on a chocolate bar of $n \times m$ squares, where $n \geq 1$ and $m \geq 1$. Initially, the chocolate bar is full. The chocolate squares are indexed from $(1,1)$ for the square at the bottom left to $(n,m)$ for the square at the top right. The players take turns making a move. A move consists of choosing a coordinate $(i,j)$ with $1 \leq i \leq n$ and $1 \leq j \leq m$ where there is still chocolate. The player making the move $(i, j)$ eats all the chocolate squares located at coordinates $(y,x)$ with $y \geq i$ and $x \geq j$. The square at coordinates $(1,1)$ is poisoned. The player who is forced to eat this square loses the game. Chomp is interesting theoretically because there is an elegant proof that the first player has a guaranteed winning strategy. The proof is based on the strategy-stealing argument. For this problem, the proof is not important, as we need to find, given $n$ and $m$, the number of possible configurations the game can reach, regardless of the way it reached that configuration or which player is currently to move. Moreover, since the committee is considerate, the result must be displayed modulo $334214459$. 

## Input data

The input file `chomp.in` contains, on the first line, the number $T \leq 100$ of tests. Each of the next $T$ lines contain two natural numbers $n$ and $m$, representing the number of rows and the number of columns for the chocolate bar in the respective test.

## Output data

In the output file `chomp.out`, for each of the $T$ tests, print on one line the number of configurations modulo $334214459$. 

## Constraints and clarifications

$1 \leq n$,     
$m \leq 128$ 

## Example

`chomp.in`    
```    
1    
2 2    
```    

`chomp.out`    
```    
6    
```