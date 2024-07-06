After his unfortunate experiences last year in Las Vegas, Charles decided never to play Blackjack again and to redeem himself by working on cleaning up the city of Copșa Mică, until recently the most polluted city in Europe. He will start by cleaning the soot production plants (the main source of pollution in the city). 

Such a network consists of $N$ boilers connected by $N$ pipes, so that each boiler is connected by pipes to exactly two other boilers, and it is possible to reach any boiler from any other following the pipes (there are exactly two ways to reach any boiler from any other). In other words, the network has the form of a simple cycle. Through each pipe $i, (1 \leq i \leq N)$ that connects boilers $a_i$ and $b_i$, a maximum water flow $d_i$ can pass. A path from a boiler $x$ to another boiler $y$ consists of a series of adjacent pipes where the first pipe in the series has one end in $x$ and the last pipe in the series has one end in $y$.

Unfortunately, Charles does not know the triplets of values $(a_i, b_i, d_i)$ that define the network's pipes, but he was able to find out for each pair of boilers $(x, y)$ what is the maximum water flow $dmax_{x,y}$ that can circulate from boiler $x$ to boiler $y$. Thus, we say that a network produces the matrix $dmax_{x,y}$ if $dmax_{x,y}$ is equal to:
* $ 0$, if $x = y$.
* the sum of the minimum flows found on each of the two paths connecting boilers $x$ and $y$. More precisely, if a path from $x$ to $y$ passes through pipes $(t_1, t_2, ..., t_k)$ and the other passes through pipes $(w_1, w_2, ... w_{n-k})$, $dmax_{x,y} = min(d_{t_1}, d_{t_2}, ... d_{t_k}) + min(d_{w_1}, d_{w_2}, ... d_{w_{n-k}})$.

# Task

Given $N$ and the matrix $dmax_{x,y}$, reconstruct a network consisting of $N$ boilers and $N$ edges defined by the triplets of values $(a_i, b_i, d_i)$ that produce the matrix $dmax_{x,y}$.

# Input data

The input file `copsamica.in` will contain on the first line a natural number $T$, signifying the number of networks in the input file. On the following lines will be the descriptions of the $T$ networks. Such a description will contain on the first line the natural number $N$. The next $N-1$ lines will contain on line $x$ as many natural numbers separated by spaces: the $y$-th number is equal to the value $dmax_{x,x + y}$.

# Output data

In the output file `copsamica.out` you will display the $T$ answers related to the $T$ networks. The answer for a pair $(N, dmax_{x,y})$ consists of $N$ lines containing three natural numbers $a_i, b_i$, and $d_i$, representing the descriptions of the $N$ edges that make up a network that produces the matrix $dmax_{x,y}$.

# Constraints and clarifications

* $ T = 5$;
* $ 3 \leq N \leq 1\ 000$;
* For $60\%$ of tests $N \leq 500$; 
* $ 1 \leq dmax_{x,y} \leq 20\ 000$;
* $dmax_{x,y} = dmax_{y,x}$ 
* The flow values $d_i$ displayed must be natural numbers $\leq 20\ 000$.
* The boilers are numbered from $1$.
* There is at least one solution. If there are multiple, you can display any of them.

# Example

`copsamica.in`
```
1
4
2 2 2
3 3
3
```

`copsamica.out`
```
1 3 1
3 2 2
2 4 2
1 4 1
```

## Explanation

For the first pair $(N,dmax_{x,y})$, we can construct the circular network consisting of the edges
$a_1 = 1, b_1 = 3, d_1 = 1$
$a_2 = 3, b_2 = 2, d_2 = 2$
$a_3 = 2, b_3 = 4, d_3 = 2$
$a_4 = 1, b_4 = 4, d_4 = 1$
This network produces the matrix $dmax_{x,y}$.
For example, $dmax_{1,3} = min(d_1) + min(d_2, d_3, d_4) = 1+1 = 2$. $dmax_{2,4} = min(d_2, d_3) + min(d_1, d_4) = 2+1 = 3$.