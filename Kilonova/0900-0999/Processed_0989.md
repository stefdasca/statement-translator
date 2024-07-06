```markdown
A digital signal represents a succession of data represented using two voltage levels called logical $0$ and logical $1$ and are found in all digital electronics, especially in computing equipment and those used for data transmission.
The graphical representation or so-called waveform of a digital signal is an uninterrupted succession of horizontal lines at level $0$ or level $1$, connected by vertical lines, as shown in the adjacent image.

~[semnal1.png|align=center]

# Task

Let $L$ be a non-zero natural number. Consider an **uninterrupted wire** of length $L$. 

Determine the number of different waveforms denoted by $U$ that can be made using this wire respecting the following properties:
* A waveform starts and ends at logic level $0$;
* A waveform uses at most two logic levels;   
* The lengths of the horizontal and vertical lines are only non-zero natural numbers;

Two waveforms are considered different if they differ by at least one line.

**Example**: For $L = 5$, $U = 8$ different waveforms can be made, as shown in the following figure:

~[semnal2.png|align=center]

# Input data

The first line will contain the natural number $L$.

# Output data

The first line will contain the remainder of the division of the natural number $U$ by $3\ 000\ 017$.

# Constraints and clarifications

* $1 \leq L \leq 10^6$;
* For $16$ points, $1 \leq L \leq 34$;
* For $20$ points, $35 \le L \leq 20\ 000$;
* For $64$ points, $20\ 001 \leq L \leq 10^6$;

# Example 1

`stdin`
```
5
```

`stdout`
```
8
```

## Explanation

$U = 8$ different waveforms can be made using a wire of length $L = 5$ respecting the required properties, as shown in the example above.

# Example 2

`stdin`
```
2022
```

`stdout`
```
177722
```

## Explanation

The remainder of the division of the number $U$ representing the number of different waveforms that can be made using a wire of length $L = 2022$ by $3000017$ is $177722$.

# Example 3

`stdin`
```
470926
```

`stdout`
```
19116
```

## Explanation

The remainder of the division of the number $U$ representing the number of different waveforms that can be made using a wire of length $L = 470926$ by $3000017$ is $19116$.
```
