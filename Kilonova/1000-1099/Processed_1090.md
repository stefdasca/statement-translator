Andra is a girl passionate about drawing. In order to improve her school performance in geometry, Andra combines her passion for drawing with solving geometry problems. Thus, on a math paper divided into squares arranged on $2^N$ lines and $2^N$ columns, Andra draws in the center a figure in the shape of a square with side $2^{N-1}$ (figure $1$). For each corner of the figure, Andra draws 4 new figures with sides equal to half of the initial figure’s side (Figure $2$). She repeats the drawing process for each new figure obtained until reaching the edge of the paper without exceeding its margins. Each square that is part of a drawn figure is colored to be distinguished on the paper. Each drawn figure is a square with its sides parallel to the edges of the paper.

~[fractal.png]

# Task

Write a program that reads the number $N$, corresponding to the $2^N \cdot 2^N$ size of the drawing paper, and determines:
1) The number of figures with the minimum side drawn;
2) The total number of squares colored at least once on the paper.

# Input data 

The input file `fractal.in` contains on the first line the natural number $C$ representing the task in the problem to be solved ($1$ or $2$) and on the second line, a natural number $N$ with the above meaning.

# Output data 

If the value of $C$ is $1$, the output file `fractal.out` will contain a natural number that represents the number of figures with the minimum side. If the value of $C$ is $2$, the output file `fractal.out` will contain a natural number that represents the total number of squares colored at least once on the paper.

# Constraints and clarifications

* $1 < N \leq 10 \ 000$
* For $30\%$ of the tests $N \leq 30$
* For correctly solving task $1$, you get $30$ points, and for correctly solving task $2$, you get $70$ points.

# Example 1

`fractal.in`
```
1
4
```

`fractal.out`
```
16
```

## Explanation

The drawing surface has $16$ lines and $16$ columns (figure $3$). Starting from the initial figure, $4$ figures will first be drawn, then $16$ figures.

# Example 2

`fractal.in`
```
1
5
```

`fractal.out`
```
64
```

## Explanation

The drawing surface has $32$ lines and $32$ columns (figure $4$). Starting from the initial figure, $4$ figures will first be drawn, then $16$ figures, respectively $64$ figures with the minimum side.

# Example 3

`fractal.in`
```
2
4
```

`fractal.out`
```
148
```

## Explanation

The drawing surface is the one from figure $3$. The number of squares colored at least once is $148$ out of a total of $256$ squares.

# Example 4

`fractal.in`
```
2
5
```

`fractal.out`
```
700
```

## Explanation

The drawing surface is the one from figure $4$. The number of squares colored at least once is $700$ out of a total of $1 \ 024$ squares.