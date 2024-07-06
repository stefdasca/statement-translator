Here is the translated text:

```markdown
Consider a sequence of $N$ cement columns (their positions are numbered from $1$ to $N$) of the same width and varying heights. They are bordered on the left (position $0$) and on the right (position $N+1$) by very tall walls. Water starts to flow from above the first column, one water unit per second. Water accumulates if there are walls on the left and right; otherwise, it flows lower to the right. Above each cement column, a water column can form, with a height equal to the number of units from the water level to the point of contact with the cement column.

# Task

1. What is the height $H$ of the tallest water column after the water has reached the height of the tallest cement column everywhere?
2. How many seconds $T$ does it take for the water to cover column number $P$?
3. What is the position $D$ of the rightmost column covered by water after $S$ seconds?
4. What is the position $R$ of the leftmost column that we can reduce by one unit so that the water reaches column $P$ as quickly as possible?

# Input data

The input file `inundatie.in` contains on the first line a natural number $C$, representing the task to be solved ($1, 2, 3$, or $4$). The second line contains the numbers $N, P$ and $S$ separated by a space with the meaning described above. The third line contains $N$ natural numbers separated by a space, representing the heights of the columns.

# Output data

The output file `inundatie.out` will contain a single number as follows:

If $C=1$: the height $H$ with the meaning above.  
If $C=2$: the time $T$ with the meaning above.  
If $C=3$: the position $D$ with the meaning above.  
If $C=4$: the position $R$ with the meaning above.  

# Constraints and clarifications

* $C \in \{1, 2, 3, 4\}$
* $3 \leq N \leq 100 \ 000$
* $1 \leq$ the height of any column in the sequence $\leq 20 \ 000$
* $1 \leq P \leq N$
* $1 \leq S \leq 100 \ 000$;
* A column of height $h$ is covered by water if the water has reached height $h$.

|#|Points|Constraints|
|-|-|--------|
|1|11|$C = 1$|
|2|25|$C = 2$|
|3|33|$C = 3$|
|4|31|$C = 4$|

# Example 1

`inundatie.in`
```
1
32 15 45
8 5 5 4 3 3 7 5 4 3 3 5 4 3 4 5 6 5 4 4 3 4 5 4 3 2 1 2 3 4 5 9
```

`inundatie.out`
```
8
```

# Example 2

`inundatie.in`
```
2
32 15 45
8 5 5 4 3 3 7 5 4 3 3 5 4 3 4 5 6 5 4 4 3 4 5 4 3 2 1 2 3 4 5 9
```

`inundatie.out`
```
21
```

# Example 3

`inundatie.in`
```
3
32 15 45
8 5 5 4 3 3 7 5 4 3 3 5 4 3 4 5 6 5 4 4 3 4 5 4 3 2 1 2 3 4 5 9
```

`inundatie.out`
```
29
```

# Example 4

`inundatie.in`
```
4
32 15 45
8 5 5 4 3 3 7 5 4 3 3 5 4 3 4 5 6 5 4 4 3 4 5 4 3 2 1 2 3 4 5 9
```

`inundatie.out`
```
7
```

## Explanations

~[inundatie.png]

All examples refer to the figure above, differing only by the task number. In all cases, $N=32, P=15$ and $S=45$.

**First example**: The orange line of height $9$ is the water level when all columns are covered by water. The tallest water column is number $27$, having $8$ water units.

**Second example**: In the above image, the red lines show the water levels when the water covers the column at position $P=15$. We observe that there are $21$ water units below the line, so it takes $21$ seconds to cover column $15$.

**Third example**: The green line shows the water level after $42$ seconds. It covers column number $29$. Letting the water flow for another $3$ seconds (up to $S=45$ seconds), the level does not rise enough to reach column $30$ because another $5$ water units are needed, that is $5$ more seconds.

**Fourth example**: The leftmost column that we will reduce by one is column number $7$. Thus, the water will reach the column $P=15$ $5$ seconds earlier. The brown line (the water line of height $6$ extending from column $2$ to column $6$) shows the $5$ units by which we reduce the time. Any other column we reduce will not reach as quickly.
```

Please review the translation and verify if it matches your needs.