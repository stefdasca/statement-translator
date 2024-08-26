## Armies

The dead will come North first. Enjoy dealing with them. We will deal with whatever is left of you. - Cersei Lannister After gathering impressive riches from soot black market deals, Charles has managed to gather an equally impressive number of enemies. And now, all $N$ armies of these enemies are on their way to the capital of Charles' kingdom, Copșa Mică. The armies are arranged in a sequence on the road, with the $i$-th army on the road consisting of $S_i$ soldiers. Since Charles is more passionate about blackjack than war, he plans to reduce his enemies by making them fight each other: at any given moment, he can scheme for two adjacent armies on the road to battle each other. Obviously, the more numerous army will win, but it will lose as many soldiers as the opposing army had. The less numerous army vanishes completely. More precisely, if the two armies have $X$ and $Y$ soldiers respectively, after the battle, a single army equal to the absolute difference between $X$ and $Y$ will remain, $|X-Y|$. If the armies have the same number of soldiers, both disappear. Charles can scheme any number of such battles. Charles wonders, for $Q$ intervals $[a, b]$ from the sequence of armies, what is the minimum number of soldiers from the armies $a, a+1, \dots, b$ that can remain, if Charles can scheme only battles between armies initially in the interval $[a, b]$.

## Input data

The input file `armate.in` will contain on the first line the numbers $N$ representing the number of armies, and $Q$ representing the number of queries. On the next line, there will be $N$ natural numbers, the $i$-th representing the number of soldiers $S_i$ in the $i$-th army. On the following $Q$ lines, there will be $Q$ pairs of numbers $a$ and $b$ representing Charles' queries.

## Output data

In the output file `armate.out` you will print $Q$ lines, representing, in order, the answers to Charles' queries.

## Constraints and clarifications

$1 \leq N \leq 400$  
$1 \leq Q \leq 800$  
$1 \leq S_i \leq 400$  
$1 \leq a \leq b \leq N$, for each of the $Q$ queries.  
An interval $[a, b]$ can appear in more than one query.  
For tests worth 30 points, $1 \leq N \leq 30$ and $1 \leq S_i \leq 30$.  
For tests worth 60 points, $1 \leq N \leq 100$ and $1 \leq S_i \leq 100$.  
For tests worth 80 points, $1 \leq N \leq 300$ and $1 \leq S_i \leq 300$.

## Example

`armate.in`  
```
4 3 
16 2 8 10 
3 4 
1 3 
1 4 
```

`armate.out`  
```
2 
6 
0 
```

## Explanation

For the first query, we look at the armies in the interval $[3, 4]$, which are (8, 10). We scheme a battle between them and obtain the sequence of armies (2). We can no longer organize another battle, so the answer is 2. 

For the second query, we look at the armies in the interval $[1, 3]$, which are (16, 2, 8). The first battle is between armies 1 and 2, obtaining the sequence (14, 8). The second battle is between the remaining armies, obtaining the sequence (6) which gives the answer.

For the third query, the sequence evolves as follows: (16, 2, 8, 10) $\rightarrow$ (16, 6, 10) $\rightarrow$ (10, 10) $\rightarrow$ (). Since we obtain the empty sequence, the answer is 0.