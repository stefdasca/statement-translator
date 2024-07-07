~[img1.jpg|align=right|width=auto] Goku has arrived in the afterlife to train for the final battle with Majin Boo. He wants to train on the $N$ planets with Kai and knows how much time it takes to travel between certain pairs of planets (he can only travel between given pairs). For each planet where he might be, he asks you to tell him the minimum duration of a path that starts from that planet and returns to the same planet, using a path that directly connects two planets at most **once**. He asked his cousin, Goku Marian, but he is struggling and needs your help.

# Input data
The first line of the input file `dbz.in` will contain the natural numbers $N$ and $M$. The next $M$ lines will have three numbers $x, y$, and $z$, indicating that there is a **bidirectional** path between planets $x$ and $y$ with a travel duration of $z$.

# Output data
The output file `dbz.out` will contain, for each planet from $1$ to $N$, the minimum duration of a path that starts from that planet and returns to the same planet, using a path that directly connects two planets at most once. If there is no such path, print the number $-1$ for that planet.

# Constraints and clarifications
* $1 \leq N \leq 1 \ 500$;
* $1 \leq M \leq 30 \ 000$;
* $1 \leq$ duration of each travel $z \leq 9 \ 000$ (it's not over $9000!$);
* For each pair of planets $(x, y)$, there is at most one direct path between them.

# Example

`dbz.in`
```
5 6 
1 2 1 
1 4 2 
4 3 4 
2 3 2 
4 5 3 
3 5 6
```

`dbz.out`
```
9 9 9 9 13
