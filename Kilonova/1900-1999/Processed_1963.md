```markdown
~[img1.jpg|align=right|widht=auto] Goku is put in an UNPRECEDENTED situation: he has to traverse a swamp with a length of $L$ (the swamp can be seen as a segment of length $L$ on the $OX$ axis). Goku, along with his friend, Krillin (who is about to die in problem $3$), has to traverse the swamp from one end to the other (they are at position $0$ and need to reach position $L$). $N$ planks are at certain distinct positions in the swamp. Since Goku cannot reach the destination directly, he will use the $N$ planks and the turtle's jumping ability. Goku can move from one plank (located at position $x$) to another plank (position $y$) if the distance between the two planks (i.e., $y - x$) is less than or equal to $D$ (where $D$ is Goku's jumping ability). Krillin has been helpful and brought $T$ additional planks (which he is carrying on his back). Determine the minimum ability $D$ necessary for Goku to reach from position $0$ to position $L$, knowing that he can place the $T$ additional planks wherever he wants.

# Input data
The input file `dragonball.in` will contain on the first line a natural number $N$, a natural number $T$, and a natural number $L$. The next $N$ lines will contain the $N$ natural numbers representing the positions of the $N$ planks.

# Output data
The output file `dragonball.out` will print the minimum ability $D$ necessary for Goku to reach from one end of the swamp to the other.

# Constraints and clarifications
* $1 \leq N, T \leq 1\ 000$;
* $1 \leq L \leq 10^{10\ 000}$;
* For $20\%$ of the tests, $L \leq 10^{9}$;
* For $40\%$ of the tests, $L \leq 10^{50}$;
* The positions of the $N$ planks are distinct, sorted in ascending order, and are within the interval $[1, L - 1]$;
* Krillin always follows Goku.

# Example

`dragonball.in`
```
5 5 100 
10 
13 
50 
69 
88
```

`dragonball.out`
```
12
```
```