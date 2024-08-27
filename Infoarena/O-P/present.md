# Present

Laika decided to give a gift to her friend Azusa, the witch from the mountains. For reasons unknown to us, the gift will be a finite set of positive integers. It would be a simple matter to choose a gift, but several factors complicate this task. First of all, Laika's enemy, Flatorte, has mysterious magical powers: given two integers $x$ and $y$, she can create the greatest common divisor of $x$ and $y$ (i.e., gcd($x$, $y$)). If Laika gives a gift in which Flatorte could add at least one element (i.e., if she offers the set $A$ where $x$, $y$ belong to $A$, but gcd($x$, $y$) does not belong to $A$), then Flatorte can immediately mock her rival. For these reasons, Laika's gift must not be able to be improved using Flatorte's powers: if she offers the set $A$, then for any $x$, $y$ that belong to $A$ it must be satisfied that gcd($x$, $y$) belongs to $A$. Secondly, Laika wants her gift to have a special significance. Exactly $K$ days have passed since she met Azusa and she wants the gift to indicate this. Therefore, Laika arranged all the sets that satisfy the condition explained above in Laikan order (explained below), thus obtaining an infinite sequence of finite sets $S_0$, $S_1$, $\dots$. She wants to select the set $S_K$ as a gift. Can you help her accomplish this task?

Laikan Order: Select two sets $A$ and $B$. Then, $A$ appears before $B$ in Laikan order if and only if $\max A < \max B$, or $\max A = \max B$ and $A - \{\max A\}$ appears before $B - \{\max B\}$ in Laikan order. For the purpose of this definition, let $\max \{\} = -\infty$. Note that this order is always well-defined for finite sets of positive integers.

## Input data

The first line of the input contains an integer $T$ - the number of tests. Each of the next $T$ lines contain a value $K$ for which we want to find $S_K$.

## Output data

For each of the $T$ values of $K$, print the set $S_K$. To print a set, print a line that starts with the number of elements of the set, followed by its elements, in increasing order.

## Constraints

$1 \leq T \leq 5$  
For 18 points, $0 \leq K \leq 100$  
For another 18 points, $0 \leq K \leq 1\,000\,000$  
For another 18 points, $0 \leq K \leq 500\,000\,000$  
For another 18 points, $0 \leq K \leq 1\,000\,000\,000$  
For the rest of the points, $0 \leq K \leq 1\,500\,000\,000$  

## Examples

`present.in`  
```
5  
0  
1  
2  
3  
4
```

`present.out`  
```
0  
1 1  
1 2  
2 1 2  
1 3
```

## Explanations

Note that $S_0 = \{\}$, $S_1 = \{1\}$, $S_2 = \{2\}$, $S_3 = \{1, 2\}$, $S_4 = \{3\}$, $S_5 = \{1, 3\}$, $S_6 = \{1, 2, 3\}$, $S_{100} = \{1, 2, 3, 7, 8\}$, $S_{1000} = \{1, 2, 3, 5, 10, 11, 12\}$. These are exactly the sets printed in the example (together with their sizes). Note that $S_6 \neq \{2, 3\}$, because $2$, $3$ belong to $\{2, 3\}$, but gcd($2$, $3$) = 1, which does not belong to $\{2, 3\}$.