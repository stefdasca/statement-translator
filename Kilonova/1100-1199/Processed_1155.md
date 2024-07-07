Let's consider a file consisting of $N$ lines, with each line containing a natural number. Initially, line $1$ contains the value $1$, line $2$ the value $2$, and so on, until line $N$ contains the value $N$.

The initial file was modified using a text editor by performing $M$ cut&paste operations. A cut&paste operation involves selecting a group of consecutive lines, removing them from their initial position, and inserting them at another position in the document.

# Task

Write a program that, for a given sequence of cut&paste operations, determines the content of the first $10$ lines of the file obtained after performing the operations.

# Input data

The first line of the input file `cutpaste.in` contains two integers $N$ and $M$. The following $M$ lines contain triplets of the form $l_i \ r_i \ p_i$, where $l_i$ and $r_i$ are the endpoints of the selected interval and $p_i$ is the position after which we insert the values.

# Output data

The output file `cutpaste.out` will contain $10$ lines, with line $i$ containing the value at position $i$ in the final sequence.

# Constraints and clarifications

* $10 \leq N \leq 100 \ 000$;
* $1 \leq M \leq 1 \ 000$;
* If $p_i = 0$, then we insert at the beginning of the document.

# Example 1

`cutpaste.in`
```
15 1
1 15 0
```

`cutpaste.out`
```
1
2
3
4
5
6
7
8
9
10
```

# Example 2

`cutpaste.in`
```
13 3
6 12 1
2 9 0
10 13 8
```

`cutpaste.out`
```
6
7
8
9
10
11
12
2
3
4
```

# Example 3

`cutpaste.in`
```
1000 6
3 7 4
1 100 57
50 60 200
63 70 500
1 800 4
7 77 98
```

`cutpaste.out`
```
801
802
803
804
101
102
36
37
38
39
