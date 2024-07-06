Ion Piețaru has a huge passion for horses. Every day, he takes them out for a walk and brings them back to the stables in the evening. However, his biggest problem is how to do this.

Ion always positions them in a straight line and, because he loves his horses and does not want to tire them, he comes up with a way to place them so as not to involve too much movement on their part. Thus, Ion puts the first $k_1$ horses in stable $1$, the next $k_2$ horses in stable $2$, and so on. Additionally, he wants no stable to remain empty among all $G$ stables, and no horse to sleep outside.

Ion Piețaru’s horses come in $2$ colors, white and bluish. Horses of different colors do not get along at all, so a stable with $i$ bluish horses and $j$ white horses will lead to a sadness of $i \times j$. The total sadness of a stable arrangement will be the sum of the sadness for all $G$ stables. Ion relies on you to help him with the arrangement of the horses.

# Task

Given $N$ and $G$, you must find the optimal way to place the $N$ horses in the $G$ stables such that the total sadness is minimal.

# Input data

The first line of the input file `despotcovit.in` contains two integers, $N$ and $G$.
The next $N$ lines contain one number each, $0$ or $1$, which represents the color of the horse ($1$ for bluish, $0$ for white).

# Output data

The first line of the output file `despotcovit.out` will contain a single integer, representing the minimum possible value of the total sadness.

# Constraints and clarifications

* $1 \leq N \leq 500$;
* $1 \leq G \leq N$;
* For tests worth $20$ points, $N \leq 50$.

# Example

`despotcovit.in`
```
6 3
1
1
0
1
0
1
```

`despotcovit.out`
```
2
```

## Explanation

We place the first $2$ horses in stable $1$ (sadness $0$), the next $3$ in stable $2$ (sadness $2$), and the last horse in stable $3$ (sadness $0$).