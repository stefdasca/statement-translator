The Border cannot be crossed easily. That's because the Dragon Arhirel (a great informatics enthusiast) does not let anyone pass unless they answer some questions...

In that country, there are $3$ types of normal pearls (we will denote them by $1$, $2$ and $3$) and $3$ types of magic pearls (we will denote them by $A$, $B$ and $C$). The magic pearls are special because they can transform into other pearls (one or more, normal or magic):
- A magic pearl of type $A$ can transform into any single normal pearl;
- A magic pearl of type $B$ can transform into a normal pearl of type $2$ and a magic pearl of type $B$, or into a normal pearl of type $1$, a magic pearl of type $A$, a normal pearl of type $3$, a magic pearl of type $A$ and a magic pearl of type $C$;
- A magic pearl of type $C$ can transform into a normal pearl of type $2$ or into a normal pearl of type $3$, a magic pearl of type $B$ and a magic pearl of type $C$ or into a normal pearl of type $1$, a normal pearl of type $2$ and a magic pearl of type $A$.

In summary, we can write the transformations as:
```
A -> 1  | 2     | 3
B -> 2B | 1A3AC
C -> 2  | 3BC   | 12A
```

The Dragon Arhirel lets us choose a magic pearl at the start (only one), and then, using only the transformations above, we have to obtain a specific sequence of normal pearls. When a magic pearl transforms, the pearls to its left and right remain the same (and in the same order). Also, the order of the resulting pearls from the transformation is exactly as presented above.

For example, if the dragon asks us to make the pearl sequence `21132123`, we can choose a magic pearl of type $B$ and follow the sequence of transformations: `B -> 2B -> 21A3AC -> 21A3A12A -> 21132123`.

Since the Dragon does not have much patience, he only asks us to say whether it is possible or not to obtain that pearl sequence.

# Task

Determine for each input sequence whether it can be obtained through the above transformations or not (choosing any initial magic pearl for each sequence).

# Input data

The input file `perle.in` contains the following structure:
* The first line contains the number $N$, representing the number of sequences in the input file;
* The next $N$ lines contain; the $i$-th line among the $N$ describes the $i$-th sequence through a succession of natural numbers separated by spaces. The first number represents the length of the sequence $L_i$, and the next $L_i$ numbers are the types of normal pearls, in order, from left to right.

# Output data

The output file `perle.out` will contain $N$ lines. Line $i$ will print a single number $1$ or $0$ ($1$ if the respective sequence (the $i$-th one) can be obtained and $0$ if it cannot be obtained).

# Constraints and clarifications

* $1 \leq N \leq 10$;
* $1 \leq L_i \leq 10\ 000$, for any $i$;

# Example

`perle.in`
```
3
8 2 1 1 3 2 1 2 3
2 2 2
1 3
```

`perle.out`
```
1
0
1
```
