# Marbles

As Christmas approaches, Algorel has taken out his red marbles from the storage boxes to decorate the tree. Since the marbles have been unused for a year and some have faded, there are multiple shades of red among them. More precisely, there are $N$ shades of red, which Algorel has numbered from $1$ to $N$. Being meticulous, he has also counted how many marbles he has for each shade -- $C_i$ for shade $i$. Algorel wants to decorate the tree with marbles of the same shade (it doesn't matter which one). Naturally, for this, he needs to repaint some marbles. Since Christmas is near, he wants to finish as quickly as possible to be ready when Santa comes. To paint a marble of shade $i$, Algorel needs to polish it for $L_i$ minutes so that the paint adheres to it. Additionally, he can paint a marble from shade $i$ to shade $j$ in $|i - j|$ minutes. Help Algorel calculate the shade in which he should paint the marbles so that the painting time is minimized.

## Task

The input file `bilute.in` contains on the first line an integer $N$. The next $N$ lines contain two numbers each, $C_i$ and $L_i$, representing the number of marbles of shade $i$ as well as the polishing time before painting for a marble of shade $i$.

## Input data

In the input file `bilute.in`, the first line contains an integer $N$. The next $N$ lines contain two numbers $C_i$ and $L_i$, representing the number of marbles of shade $i$ as well as the polishing time before painting for a marble of shade $i$.

## Output data

The output file `bilute.out` will contain two integers separated by a space, representing the number of the shade in which the marbles should be painted as well as the minimum painting time expressed in minutes. If there are multiple solutions, choose the shade with the smallest possible index.

## Constraints and clarifications

$1 \leq N \leq 30000$  
$0 \leq C_i, L_i \leq 100$  
For 50% of the tests  
$1 \leq N \leq 1000$  

## Example

`bilute.in`  
```
4
1 3
2 2
3 1
1 3
```

`bilute.out`  
```
2 15
```

## Explanation

Although the same painting time ($15$ minutes) is obtained for shade $3$, Algorel chooses shade number $2$ because it has a smaller index. The time for shade $2$ is calculated as follows:  
to paint the marble of shade $1$, it takes $1 * 3 + 1 * |1 - 2| = 4$ minutes  
the three marbles of shade $3$ are painted in $3 * 1 + 3 * |3 - 2| = 6$ minutes  
the marble of shade $4$ is painted in $1 * 3 + 1 * |4 - 2| = 5$ minutes   
in total, it takes $4 + 6 + 5 = 15$ minutes to paint all the marbles in shade $2$