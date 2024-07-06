```markdown
# Task

Tudor and Luca are two young programmers. They just finished an advanced algorithm course in C and are trying to solve problems as efficiently as possible. One of the problems they are considering states this:

- there is an array of $N$ consecutive bits numbered from $1$ to $N$ initially set to $0$
- gradually all bits will be turned into $1$ in a given order
- for each transformed bit, state the endpoints of the longest sequence of $1$s that the respective bit is part of

As Tudor found the optimal solution in a dream, Luca is paying you to solve the problem for him so as not to fall behind his friend. He asks you to be very careful due to the low limits; the more inefficient, the less money!!!

# Input data

The first line of the input file `algoritmul.in` contains a number $N$ and an array of $N$ numbers $a_1, a_2, \ldots, a_n$ representing the order in which the bits at positions $a_i$ are transformed.

# Output data

Line $i$ of the output file `algoritmul.out` will contain 2 values, left and right, representing the endpoints of the sequence that the bit at position $a_i$ is part of.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000\ 000$;
* $20$ points are awarded for $1 \leq N \leq 1\ 000$;
* $50$ points are awarded for $1 \leq N \leq 5\ 000\ 000$;
* Test 13 is just an example, so it is not scored.
* Due to the large volume of data read and written, use the parsing file from the attachments at the right of the screen.

# Example

`algoritmul.in`
```
6
3 4 1 6 2 5
```

`algoritmul.out`
```
3 3
3 4
1 1
6 6
1 4
1 6
```

## Explanation

As seen, initially the bit at position $3$ is transformed, `001000`, so the sequence it is part of is formed of it and itself. After bit $4$ is transformed, `001100`, its sequence starts at $3$ and ends at $4$. After the first bit is transformed, it is alone so it is its own sequence; thus $1$ and $1$ are displayed. The same happens until we finish with bit $5$ where all bits are connected so the sequence is the entire array, so the start is $1$ and the end is $6$.
```