# Task

Assuming there are $N$ students in the 12th grade, each distinctively numbered from $1$ to $N$ and the comment transmission relationships among the students are known, write a program that finds a way for a comment, transmitted by one of the students, to reach all students exactly once.

# Input data

The input file `coment.in` contains:
* $N$ – the number of students;
* $x_1 \\ y_1$ – student $x_1$ transmits comments to student $y_1$;
* $x_2 \\ y_2$ – student $x_2$ transmits comments to student $y_2$;
* ...;
* $x_m \\ y_m$ – student $x_m$ transmits comments to student $y_m$.

# Output data

The output file `coment.out` contains on a single line the order in which the students receive the comment. The first student is the one who transmits the comment.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $x_i,y_i \in \{1,\dots,N \}$, $\\forall i \in \{1,2,\dots,m \}$
* $m=\\frac{N \cdot (N-1)}{2}$
* Values written on the same line in the input and output files are separated by spaces.
* If there are multiple solutions, only one solution will be determined.

# Example

`coment.in`
```
4
1 2
1 4
3 1
2 4
3 2
4 3
```

`coment.out`
```
2 4 3 1
```
